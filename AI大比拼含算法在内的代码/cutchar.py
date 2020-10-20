# -*- coding: utf-8 -*-
'''
将一张图片填充为正方形后切为9张图
Author:
'''
from PIL import Image
import sys


import numpy as np

import cv2
import matplotlib.pyplot as plt



#将图片填充为正方形
def fill_image(image):
    width, height = image.size
    #选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    #生成新图片[白底]
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    #将之前的图粘贴在新图上，居中
    if width > height:#原图宽大于高，则填充图片的竖直维度
        #(x,y)二元组表示粘贴上图相对下图的起始位置
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image,(int((new_image_length - width) / 2),0))

    return new_image

#切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,3):#两重循环，生成9张图片基于原图的位置
        for j in range(0,3):
            #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list

#保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('./result/python/'+str(index) + '.png', 'PNG')
##        PIL.Image.save(filename,format)(保存指定格式的图像)
        index += 1




#找图 返回最近似的点
def search_returnPoint(img,template,template_size):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_ = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, template_,cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    # res大于70%
    loc = np.where(result >= threshold)
    # 使用灰度图像中的坐标对原始RGB图像进行标记
    point = ()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + template_size[1], pt[1] + + template_size[0]), (7, 249, 151), 2)
        point = pt
    if point==():
        return None,None,None
    return img,point[0]+ template_size[1] /2,point[1]






####Python图片转换成矩阵，矩阵数据转换成图片
##def loadImage(filenamee,xsize,ysize):
##    # 读取图片
##    im = Image.open(filenamee)
##    # 显示图片
####    im.show()  
##    im = im.convert("L") 
##    data = im.getdata()
##    data = np.matrix(data)
###     print data 
##    # 变换成512*512
##    data = np.reshape(data,(xsize,ysize))
##    
##    print("##########")
##    print(data)
##    print("##########")
##    
##    new_im = Image.fromarray(data)
##    # 显示图片
####    new_im.show()
##    return(data)





if __name__ == '__main__':
    file_path = "a_.jpg"
    image = Image.open(file_path)
##    image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)
    
##    data1=loadImage("a_.jpg",900,900)
##    data2=loadImage("8.png",300,300)
##    print(data1==data2)
##    
###矩阵对比+读出顺序出了点问题
    scale = 1

img = cv2.imread('D:/charwithoutkk/a_.png',cv2.IMREAD_GRAYSCALE)#要找的大图 ./当前目录
img = cv2.resize(img, (0,0),fx=scale,fy=scale)



 
template = cv2.imread(r'D:/resultt/8.png',cv2.IMREAD_GRAYSCALE)#图中的小图
template = cv2.resize(template,(0,0),fx=scale,fy=scale)
template_size= template.shape[:2]

##search_returnPoint(img,template,template_size)

img,x_,y_ = search_returnPoint(img,template,template_size)
if(img is None):
    print("没找到图片")
else:
    print("找到图片 位置:"+str(x_)+" " +str(y_))
    plt.figure()
    plt.imshow(img, animated=True)
    plt.show()
