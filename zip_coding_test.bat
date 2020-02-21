@echo off
@chcp 65001

set test_folder="test"
mkdir %test_folder%
cd %test_folder%

mkdir content

type nul >> "content\天地玄黃"
type nul >> "content\宇宙洪荒"
mkdir "content\いろは歌"
type nul >> "content\いろは歌\いろはにほへと"
type nul >> "content\いろは歌\いろはにほへと"
type nul >> "content\いろは歌\ちりぬるを"
type nul >> "content\The quick brown fox jumps over the lazy dog"
mkdir "content\Wow"
type nul >> "content\Wow\I can eat glass"
type nul >> "content\Wow\it does not hurt me"


:: Warining
::     It is not a test for coding,
::     but a test for ZIP Behavor in different coding environments.
::     Every coding is good and well done.

:: tl;dr

:: Test coding:
::   - CP437 (English, etc.) which defalult coding defined with zip spec;
::   - ShiftJIS (CP932, Japanese);
::   - Big5 (CP950, Traditional Chinese);
::   - GBK (CP936, Simplified Chinese);
::   - UTF-8 (CP65001).

:: Note that:
::   - CP437 only has 256 characters, of course there is no CJK character.
::   - Big5 has no Japanese characters (ex. kana, and some japanese kanji)
::   - ShiftJIS has no Chinese characters (ex. kanji that only chinese used)
::   - GBK contains all characters used in the test, but it only used in mainland China.
::   - UTF-8 is a good coding.

:: Test Env:
::     System: Windows 10,
::     Locale: English, CP437, Enable Default Unicode.
::     CMD Code page: 65001


:: No code page designated

::     (EFS: False, CP: UTF-8)
7z a test_000.zip .\content\* -mx=0
:: CP437
::     (EFS: True, CP: UTF-8)
7z a test_001_CP437.zip .\content\* -mx=0 -mcp=437
:: ShiftJIS
::     (EFS: False*, CP: ShiftJIS)
::     (With Chinese named files with EFS & UTF-8)
7z a test_002_ShiftJIS.zip .\content\* -mx=0 -mcp=932
:: Big5
::     (EFS: False*, CP: Big5)
7z a test_003_Big5.zip .\content\* -mx=0 -mcp=950
:: GBK
::     (EFS: False, CP: GBK)
7z a test_004_GBK.zip .\content\* -mx=0 -mcp=936
:: UTF-8
::     (EFS: True, CP: UTF-8)
7z a test_005_UTF-8.zip .\content\* -mx=0 -mcp=65001


:: mcu: 7-Zip uses UTF-8 for file names that contain non-ASCII symbols.
::     (EFS: True, CP: UTF-8)

:: No code page designated
7z a test_010_mcu.zip .\content\* -mx=0 -mcu=on
:: CP437
7z a test_011_mcu_CP437.zip .\content\* -mx=0 -mcu=on -mcp=437
:: ShiftJIS
7z a test_012_mcu_ShiftJIS.zip .\content\* -mx=0 -mcu=on -mcp=932
:: Big5
7z a test_013_mcu_Big5.zip .\content\* -mx=0 -mcu=on -mcp=950
:: GBK
7z a test_014_mcu_GBK.zip .\content\* -mx=0 -mcu=on -mcp=936
:: UTF-8
7z a test_015_mcu_UTF-8.zip .\content\* -mx=0 -mcu=on -mcp=65001


:: mcl: 7-Zip always uses local code page for file names.

:: No code page designated
::     (EFS: False, CP: UTF-8)
7z a test_020_mcl.zip .\content\* -mx=0 -mcl=on
:: CP437
::     (EFS: False, CP: CP437*)
::     (CJK char escape with dash `_`)
7z a test_021_mcl_CP437.zip .\content\* -mx=0 -mcl=on -mcp=437
:: ShiftJIS
::     (EFS: False, CP: ShiftJIS*)
::     (Some Chinese char escape with dash `_`)
7z a test_022_mcl_ShiftJIS.zip .\content\* -mx=0 -mcl=on -mcp=932
:: Big5
::     (EFS: False, CP: Big5*)
::     (Some Japanese char escape with dash `_`)
7z a test_023_mcl_Big5.zip .\content\* -mx=0 -mcl=on -mcp=950
:: GBK
::     (EFS: False, CP: GBK)
7z a test_024_mcl_GBK.zip .\content\* -mx=0 -mcl=on -mcp=936
:: UTF-8
::     (EFS: True, CP: UTF-8)
7z a test_025_mcl_UTF-8.zip .\content\* -mx=0 -mcl=on -mcp=65001


:: Result

:: Remember the magic spell:
::     -mcu=on


:: Reference
::   - ZIP Spec: https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
::   - 7-zip Command: https://sevenzip.osdn.jp/chm/cmdline/switches/method.htm
::   - ZIP EFS Behavor (ZH-TW): https://blog.abysm.org/2016/04/pkzip-filename-mojibake/
::   - Fix with Python: https://leeifrankjaw.github.io/articles/fix_filename_encoding_for_zip_archive_with_python.html
