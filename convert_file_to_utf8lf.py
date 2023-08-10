# Copyright (c) 2023 [aki-mia](https://github.com/aki-mia)
# 
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# ...

import sys
import os

def detect_encoding(content_bytes):
    try_encodings = ['utf-8', 'shift-jis', 'euc-jp', 'iso2022-jp']
    for enc in try_encodings:
        try:
            content_bytes.decode(enc)
            return enc
        except UnicodeDecodeError:
            continue
    return None

def process_file(filepath):
    with open(filepath, 'rb') as file:
        content_bytes = file.read()

    detected_encoding = detect_encoding(content_bytes)
    if detected_encoding is None:
        print(f"エラー: '{filepath}' のエンコーディングを検出できませんでした。")
        return

    content = content_bytes.decode(detected_encoding).replace('\r\n', '\n')
    new_filepath = os.path.join(os.path.dirname(filepath), 'check_' + os.path.basename(filepath))
    with open(new_filepath, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)
    print(f"完了: '{new_filepath}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ファイルが指定されていません。ドラッグ＆ドロップしてください。")
    else:
        for filepath in sys.argv[1:]:
            if filepath.lower().endswith('.txt') or filepath.lower().endswith('.tsv'):
                process_file(filepath)
            else:
                print(f"エラー: '{filepath}' はサポートされていないファイル形式です。")
        input("全てのファイルが処理されました。何かキーを押して終了してください。")
