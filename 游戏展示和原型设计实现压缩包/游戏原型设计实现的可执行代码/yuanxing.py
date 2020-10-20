import random
import os
import simpleguitk as simplegui
import PySimpleGUI as sg
from PIL import Image 


# 随机选取一张图片
def GetImagePath(filepath):
	imgs = os.listdir(filepath)
	if len(imgs) == 0:
		print('[Error]: No pictures in filepath...')
	return os.path.join(filepath, random.choice(imgs))


# 设置画布尺寸
w = 600
h = w + 100

# 定义图像块的边长
image_size = w / 3

# 定义图像块坐标列表
all_coordinates = [[image_size * 0.5, image_size * 0.5], [image_size * 1.5, image_size * 0.5],
                   [image_size * 2.5, image_size * 0.5], [image_size * 0.5, image_size * 1.5],
                   [image_size * 1.5, image_size * 1.5], [image_size * 2.5, image_size * 1.5],
                   [image_size * 0.5, image_size * 2.5], [image_size * 1.5, image_size * 2.5], None
                   ]
squar_center = [[image_size * 0.5, image_size * 0.5], [image_size * 1.5, image_size * 0.5],
                   [image_size * 2.5, image_size * 0.5], [image_size * 0.5, image_size * 1.5],
                   [image_size * 1.5, image_size * 1.5], [image_size * 2.5, image_size * 1.5],
                   [image_size * 0.5, image_size * 2.5], [image_size * 1.5, image_size * 2.5], None
                   ]
# 棋盘的行列
row = 3
col = 3

# 定义步数
steps = 0

#是否完成
#finish = False

# 保存所有图像块的列表
board = [[None, None, None], [None, None, None], [None, None, None]]
yuan = [[None, None, None], [None, None, None], [None, None, None]]
#load那个函数参数是路径
# 1.设置图像,载入图像
im = Image.open(GetImagePath('./pictures'))
imBackground = im.resize((600,600))
imBackground.save('pic22.bmp','BMP')
baymax = simplegui.load_image('pic22.bmp') # pic.bmp
# 可以：https://images.cnblogs.com/cnblogs_com/kukicookie/1842259/o_200907100833untitled.png
# 可以：http://img.netbian.com/file/2020/0130/c5d20fe416022a3d72be820e76bfba9b.jpg
# 不可以：D:\python_files\pic.bmp
#此处修改了simplegui里的image.py，实现本地图片也能用


# 定义一个图像块的类
class Square:
    # 定义一个构造函数，用于初始化
    def __init__(self, coordinate):
        self.center = coordinate
 
    # 绘制图像的方法
    def draw(self, canvas, board_pos):
        canvas.draw_image(baymax, self.center, [image_size, image_size],
                       [(board_pos[1] + 0.5) * image_size, (board_pos[0] + 0.5) * image_size],
                       [image_size, image_size])

# 定义一个方法进行拼接
def init_board():
    #print(all_coordinates) #buquedall_coordinates是有图像块的地方的坐标，图像没有标号
    '''
    #存下正确的坐标
    #(没法存下正确的坐标，因为Square是一串东西，应当从all_coordinates入手，
    #因为不管怎么打乱，all_coordinates里边存的图像都是原本的坐标)
    for i in range(row):
        for j in range(col):
            idx = i * row + j
            squar_center = all_coordinates[idx]
            print(squar_center)
            if squar_center is None:
                yuan[i][j] = None
            else:
                yuan[i][j] = Square(squar_center)
                print(yuan[i][j])
    '''
    random.shuffle(all_coordinates)  # 打乱图像
    # 填充并且拼接图版
    for i in range(row):
        for j in range(col):
            idx = i * row + j
            squar_center = all_coordinates[idx]
            #print(squar_center)
            #squar_center的值就是图像块正确放置的坐标(竖,横)
         # 如果坐标值是空的，让该框为空
            if squar_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(squar_center)
                #print(board[i][j])
                #print(i)
                #print(j) ij也是有图像块的坐标
 
def play_game():
    global steps
    steps = 0
    init_board()
def draw(canvas):  # 画步数
    canvas.draw_image(baymax, [w / 2, h / 2], [w, h], [52, w + 60.5], [100, 120])
    canvas.draw_text('步数：' + str(steps), [470, 621], 20, 'white')  # 64分钟
    # 绘制游戏界面各元素
    for i in range(row):
        for j in range(col):
            if board[i][j] is not None:
                board[i][j].draw(canvas, [i, j])

def mouseclick(pos):
    global steps
    # 将点击的位置换算成拼接板上的坐标
    r = int(pos[1] / image_size)
    c = int(pos[0] / image_size)
    if r < 3 and c < 3:
        if squar_center != all_coordinates:
         if board[r][c] is None:  # 表示点击的是一个空白位置
             return
         else:
             # 检查上下左右是否有空位置，有则移动过去
             current_square = board[r][c]
             if r - 1 >= 0 and board[r - 1][c] is None:  # 判断上面
                 board[r][c] = None
                 board[r - 1][c] = current_square
                 #print(r)
                 #print(all_coordinates[0])
                 all_coordinates[(r-1)*3+c] = all_coordinates[r*3+c]
                 all_coordinates[r*3+c] = None
                 steps += 1
             elif c + 1 <= 2 and board[r][c + 1] is None:  # 判断右边
                 board[r][c] = None
                 board[r][c + 1] = current_square
                 #print(current_square)
                 all_coordinates[r*3+c+1] = all_coordinates[r*3+c]
                 all_coordinates[r*3+c] = None
                 steps += 1
             elif r + 1 <= 2 and board[r + 1][c] is None:  # 判断下边
                 board[r][c] = None
                 board[r + 1][c] = current_square
                 #print(current_square)
                 all_coordinates[(r+1)*3+c] = all_coordinates[r*3+c]
                 all_coordinates[r*3+c] = None
                 steps += 1
             elif c - 1 >= 0 and board[r][c - 1] is None:  # 判断左边
                 board[r][c] = None
                 board[r][c - 1] = current_square
                 #print(current_square)
                 all_coordinates[r*3+c-1] = all_coordinates[r*3+c]
                 all_coordinates[r*3+c] = None
                 steps += 1
    else :
         canvas.draw_image(baymax, [w/2 , h/2 ], [w , h ], [300, w -250], [600, 700])             

    

# 是否完成
def isFinished(all_coordinates):
  for i in range(row*col-1):
    if squar_center[i] != all_coordinates[i]:
        #print(squar_center)
        #print(all_coordinates)
        #print(finish)
        return False
  return True



frame = simplegui.create_frame("拼图游戏", w, h)
frame.set_canvas_background('Pink')

#frame.set_draw_handler(draw)
frame.add_button('重新开始', play_game, 60)
 #frame.add_button('更换图片', main, 60)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)
#frame.set_draw_handler(draw)
play_game()
frame.start()   



