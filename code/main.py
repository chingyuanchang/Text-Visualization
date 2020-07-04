# 导入扩展库
import os
import WordSegment
import plotWordcloud


if __name__=='__main__':

# 读取文件
    path = os.path.join('data','subsection9.txt')
    #fn = open(path,encoding='gb18030',errors='ignore') # 打开文件
    fn = open(path,encoding='utf-8',errors='ignore') # 打开文件
    text = fn.read() # 读出整个文件
    fn.close() # 关闭文件
    
    text = text.lower()
    text=WordSegment.word_segment(text)

    
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
