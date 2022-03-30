'''
@Author: aponder
@Date: 2020-04-08 17:51:46
@LastEditors: aponder
@LastEditTime: 2020-04-10 17:57:01
@FilePath: /pdf2txt/main.py
'''
import sys
from pathlib import Path


def pdf2txt(pdf_path):
    from pdfminer.high_level import extract_text_to_fp

    if sys.version_info > (3, 0):
        from io import StringIO
    else:
        from io import BytesIO as StringIO
    output_string = StringIO()
    with open(pdf_path, 'rb') as fin:
        extract_text_to_fp(fin, output_string)
    # output_string = extract_text('test.pdf')
    # print(output_string)
    # print(output_string.getvalue().strip())
    return output_string.getvalue()


def main():
    folder = Path('pdfs')
    for f in folder.iterdir():
        file_name = str(f.absolute())
        txt_name = file_name[:-4] + '.txt'
        if '.pdf' in file_name:
            Path(txt_name).write_text(pdf2txt(file_name), encoding='utf8')


if __name__ == '__main__':
    main()
