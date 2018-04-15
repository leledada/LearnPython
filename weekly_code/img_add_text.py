#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

setFont = ImageFont.truetype(r"happyfont2016.ttf", 50)  # 这里我之前使用Arial.ttf时不能打出中文，用华文细黑就可以
fillColor = "#ff0000"
image = Image.open("yuantu.jpg")
draw = ImageDraw.Draw(image)
width, height = image.size
draw.text((40, height - 90), u'陈独秀你坐下！！', font=setFont, fill=fillColor)
image.save("yuantu.jpg", 'jpeg')
