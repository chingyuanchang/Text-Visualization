# 导入扩展库
from os import path
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import numpy as np # numpy数据处理库
import wordcloud # 词云展示库
from wordcloud import WordCloud



def generate_wordcloud(text):
    '''
    输入文本生成词云
    '''
    # 设置显示方式
    mask = np.array(Image.open('Images/Alfred Sisley.jpg'))# 定义词频背景
    #mask = np.array(Image.open('Images/alice.png'))# 定义词频背景
    #wc = WordCloud(width=600, height=400, background_color="white", max_words=4000)
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=10, # 词云显示的最大词数  
           mask=mask,# 设置背景图片 
           font_path='C:/Windows/Fonts/simhei.ttf',# 设置字体格式
           max_font_size=2000 # 字体最大值
                  )

    # 生成词云 
    wc.generate_from_frequencies(text)
    #image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
    #wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案

    # 生成的词云图像保存到本地
    wc.to_file(path.join("Images//cloud.jpg"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()# 在IDE中显示图片

