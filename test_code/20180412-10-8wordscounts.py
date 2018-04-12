#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

word_list = []
file = 'english_words.txt'
with open(file, 'r', encoding='utf8') as f:
    lines = f.readlines()

for line in lines:
    word_list[len(word_list):len(word_list)] = line

print(''.join(word_list))

result_list = re.findall(r'\b\w+\b', ''.join(word_list))

print(result_list)
print('there are %d words in %s' % (len(result_list),file))
