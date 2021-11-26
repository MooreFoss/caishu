# coding:utf-8
# by lmh
from random import *
from time import *

ws = int(input("请输入猜数的位数(1-10)\n"))
while ws < 1 or ws > 10:
    ws = int(input("输入错误！请重新输入猜数的位数(1-10)\n"))
# 检查输入
x = randint(10 ** (ws - 1), 10 ** ws)
# 取随机数
xlist = list(str(x))
print(xlist)
alist = []
while True:
    out = ""
    i = 0
    # 初始化
    a = int(input("请输入你的猜想:\n"))
    alist = list(str(a))
    while len(alist) != ws:
        a = int(input("请输入位数正确的整数:" + str(ws) + "位\n"))
        alist = list(str(x))
    # 取随机数
    if alist == xlist:
        break
    else:
        while i < int(len(alist)) and i < int(len(xlist)):
            if alist[i] == xlist[i]:
                out = out + "第" + str(i + 1) + "位正确，此位为" + str(xlist[i]) + "\n"
            i = i + 1
        # 对比列表
        if out == "":
            print("很抱歉，一个数字也没有猜对。\n再试试吧！")
        else:
            print(out)
        # 输出结果
print("猜对了！是" + str(x) + "!\n")
print("将在10秒后退出\n")
sleep(10)
quit()
