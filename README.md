# Requirements：  
Word Cloud  
Text source: TopicStream Paper: https://arxiv.org/pdf/1512.04042.pdf   
Treat the entire document as a corpus, treat each subsection as a document   
Text Analysis  
Tokenization  
TF Model: Term frequency  
TF-IDF Model: Inverse document index   
Report K-D vector for (word, significance)  
The k mostly occurred words in a document   
The k most significant words (TF-IDF) in a document   
# 设计思路
整个设计分为三部分：  
1）	主程序：将要分析的文档导入程序中，注意使用open()读取英文数据用utf-8，并将字母都转为小写；  
2）	词频分析：对文档进行分析，统计每个单词出现的次数并进行排序，要排除各种干扰项比如数字和标点符号，并且对常用的单词比如介词和代词冠词进行终止化处理，不加入最终显示的队列中，还要注意同一个单词的单数和复数形式；  
3）	词云展示：将排好序的单词进行可视化，仅可视化前k个；  
# 实验结果如下：
图1为整篇文章中出现次数最多的10个词的词云；图2为去除常用词后出现最多的10个词的词云。  
可以发现去除常用词后能够更加清楚地看出整篇文章讨论了哪些内容。   
https://github.com/chingyuanchang/Text-Visualization/blob/master/images/1.jpg
图1：整篇文章，未去除            
https://github.com/chingyuanchang/Text-Visualization/blob/master/images/2.jpg
图2：整篇文章，去除后
