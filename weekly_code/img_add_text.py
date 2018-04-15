#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

setFont = ImageFont.truetype(r"happyfont2016.ttf", 50)  # 站酷快乐体
fillColor = "#ff0000"
image = Image.open("yuantu.jpg")
draw = ImageDraw.Draw(image)
width, height = image.size
draw.text((40, height - 90), u'陈独秀你坐下！！', font=setFont, fill=fillColor)
image.save("yuantu.jpg", 'jpeg')
