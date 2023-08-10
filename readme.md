# File Encoding Converter

Copyright (c) 2023 [aki-mia](https://github.com/aki-mia)

このツールは、指定された .txt または .tsv ファイルの改行コードをLFに変換し、文字コードをUTF-8 (BOMなし) に変換した上で、ファイル名の冒頭に`check_`をつけて同じディレクトリに新しいファイルとして保存します。

## ライセンス

本プロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 動作環境
- OS: Windows 10 Proで動作確認をしています。
- Python 3.10.12

## ビルド方法（pyinstaller）

`poetry install`で必要なパッケージを導入後に以下手順を実施します。

1. プロジェクトのルートディレクトリに移動します。
2. 以下のコマンドを実行して、ビルドを開始します。

```
pyinstaller convert_file_to_utf8lf.py --onefile --clean
```

3. `dist`ディレクトリの中にビルドされた実行ファイル（convert_file_to_utf8lf.exe）が生成されます。

## 使用方法
1. `convert_file_to_utf8lf.exe`ファイルに変換したい .txt または .tsv ファイルをドラッグ＆ドロップします。
2. 処理が完了すると、同じディレクトリに「check_元ファイル名.tsv」というファイル名で保存されます。
3. エラーが発生した場合は`error.txt`ファイルが生成されます。

### 注意事項
- このツールは、元のファイルがUTF-8、Shift-JIS(ANSI)　、EUC-JP、ISO2022-JPのいずれかで動作します。エンコーディングを自動検出してLFに改行コードを変換し、UTF-8（BOMなし）で保存します。タブ区切りであることの確認はしません。
- .txt または .tsv ファイルのみを受け付けます。

### 免責事項
- 本ソフトウェアは「現状有姿」で提供され、明示的または黙示的な保証は一切ありません。特に、商品性、特定目的への適合性、第三者の権利を侵害しないことに対する黙示的な保証も含まれません。本ソフトウェアの使用に関連するリスクは、ユーザー自身の責任とします。

- 作者は本ソフトウェアに関連するサポートを提供せず、また、使用により生じた損害に対して一切の責任を負いません。ユーザーは、本ソフトウェアを自己の責任で使用するものとし、それにより生じたいかなる損害に対しても作者は一切の責任を負わないものとします。

### 作者について
- Github: [aki-mia](https://github.com/aki-mia)
- Linkedin: [Akihiro Tanii](https://www.linkedin.com/in/akihirotanii/)

### バージョン情報
- 現在のバージョン: 1.0.0
- 最終更新日: 2023-08-10

---

English Translation

# File Encoding Converter

Copyright (c) 2023 [aki-mia](https://github.com/aki-mia)

This tool converts the newline code of a given .txt or .tsv file to LF and the character encoding to UTF-8 (no BOM), then saves it as a new file in the same directory with the file name prefixed with `check_`.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Operating Environment
- OS: Windows 10 Pro has been tested.
- Python 3.10.12

## How to build (pyinstaller)

After installing the necessary packages with `poetry install`, follow the steps below.

1. Go to the root directory of the project.
2. Execute the following command to start the build.

```
pyinstaller convert_file_to_utf8lf.py --onefile --clean
```

3. a built executable file (convert_file_to_utf8lf.exe) will be generated in the `dist` directory.

## Usage.
1. drag and drop the .txt or .tsv file you wish to convert into the `convert_file_to_utf8lf.exe` file 2.
When the process is completed, the file will be saved in the same directory with the file name "check_source_filename.tsv". 3.
3. an `error.txt` file will be generated if an error occurs.

### Notes
- This tool works when the original file is UTF-8, Shift-JIS(ANSI), EUC-JP, or ISO2022-JP. It automatically detects the encoding, converts the line feed code to LF, and saves the file as UTF-8 (without BOM). It does not check that the file is tab delimited.
- Only accepts .txt or .tsv files.

### Disclaimer
- This software is provided "AS IS" and without warranty of any kind, either express or implied. In particular, this does not include any implied warranties of merchantability, fitness for a particular purpose, or non-infringement of third party rights. the risks associated with the use of this software are the sole responsibility of the user.

- The author provides no support related to this software and assumes no responsibility for any damages resulting from its use. The user shall use this software at his/her own risk and the author shall not be liable for any damages resulting from the use of this software.

### About the Author
- Github: [aki-mia](https://github.com/aki-mia)
- Linkedin: [Akihiro Tanii](https://www.linkedin.com/in/akihirotanii/)

### Version Information
- Current version: 1.0.0
- Last updated: 2023-08-10
