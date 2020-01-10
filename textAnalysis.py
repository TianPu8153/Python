from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt  #绘制图像的模块
import  jieba                    #jieba分词
import numpy as np # numpy数据处理库
from PIL import Image # 图像处理库
# from scipy.misc import imread


path_txt='C://Users//Administrator//Desktop//talk2.txt'
f = open(path_txt,'r',encoding='UTF-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(f))
mask =plt.imread('2.jpg')
#mask = np.array(Image.open('C://Users//Administrator//Desktop//2.png')) # 定义词频背景
wc = WordCloud(
    # background_color='white',# 设置背景颜色
    mask=mask,# 设置背景图片
    font_path='C:\\Windows\\Fonts\\STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=2000, # 设置最大现实的字数
    #stopwords=STOPWORDS,# 设置停用词
    # max_font_size=150,# 设置字体最大值
    random_state=60,# 设置有多少种随机生成状态，即有多少种配色方案
    background_color=None, 
    prefer_horizontal=1.5,
    scale=3,
    mode="RGBA"
)
wc.generate_from_text(cut_text)
print('开始加载文本')
#改变字体颜色
# img_colors = ImageColorGenerator(mask)
#字体颜色为背景图片的颜色
# wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
