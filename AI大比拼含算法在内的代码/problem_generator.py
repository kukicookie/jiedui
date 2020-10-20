import numpy as np

import random




def random_pintu(xsize, ysize):

    a = np.arange(0, xsize * ysize).reshape(xsize, ysize)  ##  1.arange(起点（默认0），终点+1（0起点的话就是个数了），步长（默认1）)  reshape()将一维数组转换为多维数组      返回值： np.arange()函数返回一个有终点和起点的固定步长的排列（等差数组？），如[1,2,3,4,5]，起点是1，终点是5，步长为1。 

    # 为确保有解，进行打乱

    for i in range(xsize):

        for j in range(ysize):

            a[i][j] = (a[i][j] + 1) % (xsize * ysize)

    space = xsize - 1, ysize - 1   ##   print(type(space)) 不懂的敲敲代码就知道了  Python 的元组tuple与列表类似，不同之处在于元组的元素不能修改。  元组使用小括号(,,,,)[也可不要（）]，列表使用方括号[,,,]。  元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

    for i in range(xsize * ysize * 16):
##        print('****')
        di = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        x, y = space[0] + di[0], space[1] + di[1]
##        print(di)
##        print(x,y)
        if xsize > x >= 0 and ysize > y >= 0:

            a[x, y], a[space[0], space[1]] = a[space[0], space[1]], a[x, y]
##            print(space[0], space[1])

            space = x, y
##            print(space)
##            print('****')
    return a

##rr=random_pintu(3,3)
##print(rr)
##
##r=random_pintu(3,3)
##print(r)
