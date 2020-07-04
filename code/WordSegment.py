# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 中文分词库
from os import path
from collections import Counter

def word_segment(string_data):

    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all = False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    object_list = []
    remove_words = [u' ',u'\n',u'[', u']',u',',u'”',u'“', u'?',u'!', u'/', u'=', u'.',u'"',u':',u';',u'+',u'-',u'*',u'/',u'%',u'&',u'(',u')',
                    u'@',u'#',u'!',u'~',u'—',u'–',u'−',u'⋯',u'φ',
                    u'to',u'from',u'by',u'for',u'with',u'on',u'in',u'In',u'at',u'between',u'the',u'The',u'and',u'of',u'with',u'as',u'over',u'into',
                    u'A',u'a',u'an',u'we',u'it',u'We',u'this',u'that',u'their',u'our',u'ours',u'help',u'well',u'such',
                    u'can',u'is',u'are',u'be',u'was',u'were',u'stop',u'each',u'which',u'have',u'has',u'been',u'may',
                    u'0',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'14',u'25',u'13',u'16',u'19',
                    u'22',u'28',u'31',u'34',u'36',u'37',u'40',u'43',u'46',u'49',u'52',u'55',u'58',
                    u'first',u'second',u'one',u'two',u'ebola',u'africa',u'focus',u'new',u'how',u'document',
                    u'pages',u'opinion',u'example',u'confidence',u'obama',u'future',u'explore',u'no',
                    u'cut',u'cuts',u'topics',u'trees',u'time',u'text',u'cuts',u'tree',u'topic',u'node',u'nodes',u'data',u'public',u'based',u'number',u'news',
                    u'fig',u'ft',u'df',u'p1',u'p2',
                    u'a',u'b',u'c',u'd',u'e',u'f',u'g',u'h',u'j',u'k',u'm',u'p',u'r',u's',u't',u'w',u'x',u'y',u'ti',u'nmi'] # 自定义去除词库
    data=[]
    for word in seg_list_exact: # 循环读出每个分词
        data.append(word)
        if word not in remove_words: # 如果不在去除词库中
            object_list.append(word) # 分词追加到列表
    dataDict=Counter(data)
    with open('data//词频统计.txt','w',encoding='utf-8',errors='ignore') as fw:
        for k,v in dataDict.items():
            fw.write("%s,%d\n" % (k,v))

            
    # 词频统计
    word_counts = collections.Counter(object_list) # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
    print (word_counts_top10) # 输出检查
    return word_counts