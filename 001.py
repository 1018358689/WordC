#!/usr/bin/env python
# -*- coding:utf-8 -*-

import jieba
from wordcloud import WordCloud, ImageColorGenerator, random_color_func
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image
import re

with open('poetry.txt', encoding='utf-8') as f:  #'杭师大教育学院交流群.txt'
    text = f.read()

text = re.sub('((\d){4}-(\d){2}-(\d){2} (\d){1,2}:\d\d:\d\d)|\[图片\]|\[表情\]|\s|系统消息\(10000\)', '', text)

wl = jieba.cut(text, cut_all=True)
wl = ' '.join(wl)

pig_pic = np.array(Image.open('pig.png'))

my_wordcloud = WordCloud(
    background_color='white',  # 设置背景颜色
    mask=pig_pic,  # 设置背景图片
    max_words=5555,  # 设置最大显示的字数
    width=1024,
    height=768,
    margin=6,
    # stopwords=STOPWORDS,  # 设置停用词
    max_font_size=111,  # 设置字体最大值
    # random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
    font_path='msyh.ttc'  # 字体位置
)
my_wordcloud.generate(wl)

# image_color = ImageColorGenerator(pig_pic)   #这两行是颜色跟随图片
# plt.imshow(my_wordcloud.recolor(color_func=image_color))
plt.imshow(my_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
my_wordcloud.to_file('1.png')  # 有mask 就根据mask大小 否则根据width&height
