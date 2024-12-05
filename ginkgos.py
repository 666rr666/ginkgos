import turtle as T
import random
import time

def tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('yellow')  # 黄色
            else:
                t.color('orange')  # 橘黄色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('orange')
            else:
                t.color('yellow')
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branch - 10 * b, t)
        t.left(40 * a)
        tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣
def Petal(m, t):
    # 绘制落叶的函数
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('yellow') # 落叶的颜色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg ='wheat')  # wheat 小麦色
t.left(90)

# 在画布上绘制文字
t.penup()
t.goto(0, -200)  # 设置文字绘制的起始位置
t.pendown()
t.write("又是一年银杏季", align="center", font=("STCaiyun", 25, "normal"))#字体+字号+加粗bold正常normal

t.penup()
t.goto(0, -250)  # 设置文字绘制的起始位置
t.pendown()
t.write("夏天的遗憾一定会被秋天的风所吹散", align="center", font=("Microsoft YaHei", 20,"normal"))#字体+字号+加粗

# 绘制多棵树
for i in range(3):  # 控制绘制几棵树
    t.penup()
    # 随机设置树的起始位置
    t.goto(random.randint(-300, 300), -100)
    t.pendown()
    t.color('sienna')
    tree(60, t)  # 绘制每棵树
    Petal(100, t)

# 结束
w.exitonclick()
