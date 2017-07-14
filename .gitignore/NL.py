# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:54:09 2017

@author: a550859
"""

import nltk
text="Mary had a little lamb.Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize
sents = sent_tokenize(text)
print (sents)