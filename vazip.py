import os
import os.path
import shutil
import logging
import zipfile
import click
import functools


__version__ = '0.1.0'

span = functools.partial(print, end='')
logging.basicConfig(level=logging.WARNING)

default_config = {
    "coding": "CP437",
    "ignore-efs": False, 
    "yes": True,
}

text = {
    "extract_confirm": "Are they readable?",
    "extract_confirm_yes": "UwU",
    "option_extract_metavar": "<DIR>", 
    "option_extract_help": "Extract the zip file to <DIR>.", 
    "option_coding_metavar": "<CODEC>", 
    "option_coding_help": "Python acceptable code page string, listed here: \"https://docs.python.org/3/library/codecs.html#standard-encodings\".", 
    "option_password_metavar": "<PWD>", 
    "option_password_help": "When extracting, password is required if the zip file is encrypted.", 
    "option_separate_help": "Extract the zip file to separate folder.", 
    "option_ignore-efs_help": "Ignore EFS flag.", 
    "option_yes_help": "Ignore confirmation before extraction.", 
    "option_debug_help": "tl;dr", 
    "command_main_help": "vaZip -- unzip with a specific code page.",
}


@click.command(help=text["command_main_help"])
@click.help_option('-h', '--help')
@click.version_option(__version__, '-v', '--version')
@click.argument('zip_file', type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False, readable=True))
@click.option('-e', '--extract', type=click.Path(exists=False, file_okay=False, dir_okay=True, writable=True), 
                metavar=text["option_extract_metavar"], help=text["option_extract_help"])
@click.option('-c', '--coding', default=default_config["coding"], show_default=True, 
                metavar=text["option_coding_metavar"], help=text["option_coding_help"])
@click.option('-p', '--pwd', '--password', 'password',
                metavar=text["option_password_metavar"], help=text["option_password_help"])
@click.option('-s', '--separate', is_flag=True, help=text["option_separate_help"])
@click.option('--ignore-efs', is_flag=True, default=default_config["ignore-efs"], show_default=True, 
                help=text["option_ignore-efs_help"])
@click.option('--yes', is_flag=True, default=False, help=text["option_yes_help"])
@click.option('--debug', is_flag=True, default=False, help=text["option_debug_help"])
def main(zip_file, extract, coding, password, separate, ignore_efs, yes, debug):
    if debug: logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(f'zip_file = {zip_file}')
    logging.debug(f'extract = {extract}')
    logging.debug(f'coding = {coding}')
    logging.debug(f'password = {password}')
    logging.debug(f'separate = {separate}')
    logging.debug(f'ignore_efs = {ignore_efs}')
    logging.debug(f'yes = {yes}')
    logging.debug(f'debug = {debug}')

    with zipfile.ZipFile(zip_file) as zp:
        print('EUD Filename')
        namelist_reen = []
        for info in zp.infolist():
            is_encrypted = info.flag_bits & 0b0000000000000001  # Bit 00
            is_efs = info.flag_bits & 0b0000100000000000  # Bit 11
            span('E' if is_encrypted else '-')
            span('U' if is_efs else '-')
            span('D' if info.is_dir() else '-')
            span(' ')

            filename_read = info.filename  # str, UTF-8 if EFS, else CP437
            if is_efs and not ignore_efs:
                filename_reen = filename_read
            else:
                filename_read_coding = 'UTF-8' if is_efs else 'CP437'
                filename_byte = filename_read.encode(filename_read_coding)
                filename_reen = filename_byte.decode(coding)

            print(filename_reen)
            namelist_reen.append(filename_reen)

        if extract:
            if not yes:
                if not click.confirm(f'{text["extract_confirm"]}'): return 1  # EXIT CODE
            else:
                print(f'{text["extract_confirm"]} [y/N]: {text["extract_confirm_yes"]}')
            
            if separate:
                zp_file_root, _ = os.path.splitext(os.path.basename(zip_file))
                extract = os.path.join(extract, zp_file_root)
                logging.debug(f'zp_file_root = {zp_file_root}')
                logging.debug(f'extract = {extract}')

            logging.debug(f'len(zp.infolist()) = {len(zp.infolist())}')
            logging.debug(f'len(namelist_reen) = {len(namelist_reen)}')
            for i, zipper in enumerate(zip(zp.infolist(), namelist_reen)):
                info, filename_reen = zipper
                target_path = os.path.join(extract, filename_reen)
                target_path = os.path.normpath(target_path)
                upper_dirs = os.path.dirname(target_path)
                if upper_dirs and not os.path.exists(upper_dirs):
                    os.makedirs(upper_dirs)
        
                span(f'Extractiing {i+1:4d}/{len(zp.infolist()):<4d}: {target_path} ... ')
                if info.is_dir():
                    if not os.path.isdir(target_path):
                        os.mkdir(target_path)
                    print('mkdir.')
                    continue
                if os.path.exists(target_path):
                    print('file exists.')
                    continue
                pwd = None if not password else password.encode(coding)
                with zp.open(info, pwd=pwd) as src, open(target_path, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                    print('done.')


if __name__ == "__main__":
    main()
