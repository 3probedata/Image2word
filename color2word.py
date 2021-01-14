#!/usr/bin/env python
# coding=utf-8
from PIL import Image
import argparse
# 命令列輸入引數處理
parser = argparse.ArgumentParser()
parser.add_argument('file')# 輸入檔案
parser.add_argument('-o', '--output')# 輸出檔案
parser.add_argument('--width', type=int, default=110)# 輸出字元畫寬
parser.add_argument('--height', type=int, default=80)# 輸出字元畫高
# 獲取引數
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 使用來轉換的字元串
#ascii_char = list("0123456789A.CDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#&;:-,.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#&;:-,.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#&;:-,.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi.")# 將256灰度對映到70個字元上
ascii_char = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#&;:-,.")
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

def get_gray_char(gray, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    #gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    #unit = (256.0 + 1) / length
    return ascii_char[int(gray)] # int(gray / unit)

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            #txt += get_gray_char(im.getpixel((j, i))) # gray
            txt += get_char(*im.getpixel((j, i))) # color
        txt += '\n'
        print(txt)

    # 字元畫輸出到檔案
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)