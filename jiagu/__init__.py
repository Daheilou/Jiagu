#!/usr/bin/env python
# -*-coding:utf-8-*-
from jiagu import analyze
from jiagu.mmseg import MMSeg
any = analyze.Analyze()

init = any.init

# 分词
seg = any.cws
cws = any.cws
cut = any.cws

# # MMSEG 分词
# mmseg = MMSeg().cws

# 词性标注
pos = any.pos

# 命名实体识别
ner = any.ner

# 其他组合
seg_pos = any.cws_pos
seg_pos_ner = any.cws_pos_ner


keywords = any.keywords
