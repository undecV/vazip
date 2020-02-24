# vaZip

解壓縮 *亂碼* 的 ZIP 檔案。

> ⚠️ 這是**預發行**版本。</ br>
> 🛑 請先備份檔案再試用。

Readme Languages: [English](readme.md), [正體中文](readme_zh.md)

## 安裝

0. Python 3
1. `git clone`
2. `cd`
3. `pip install .`

## 如何使用

參見 `vazip --help`.

```txt
用法: vazip [選項] 壓縮檔名

  vaZip -- 使用特定的內碼表解壓縮

選項:
  -h, --help                   顯示幫助訊息並退出。
  -v, --version                顯示版本訊息並退出。
  -e, --extract <DIR>          解壓縮 Zip 檔案到 <DIR>.
  -c, --coding <CODEC>         Python 接受的內碼表（code page）字串，列在這裡：
                               "https://docs.python.org/3/library/codecs
                               .html#standard-encodings".  [預設值: CP437]
  -p, --pwd, --password <PWD>  解壓縮時，加密檔案需要密碼。
  -s, --separate               解壓縮到單獨的資料夾中。
  --ignore-efs                 無視 EFS flag.  [預設值: False]
  --yes                        忽略解壓縮前的確認。
  --debug                      除錯資訊，不要看。
```

示例.1 使用內碼 ShiftJIS 列出檔案

```cmd
vazip "壓縮檔.zip" -c shiftjis
```

示例.2 解壓縮到當前工作目錄

```cmd
vazip "壓縮檔.zip" -c shiftjis -e .
```

示例.3 解壓縮到單獨的資料夾 (目標在 `./壓縮檔/*`)

```cmd
vazip "壓縮檔.zip" -c shiftjis -e . -s
```
