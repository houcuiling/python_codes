# import 导入   python包
# random 随机数
import random
# math 数学包
import math
# time 时间
import time

print(math.log(44))
print(math.cos(3.14159))

# 注释
# print 打印
print("这是一个骰子模拟器")

# 变量 x 
x = "y"
print(x)

if x == "y":
    print("ok")
else:
    print("error")

cishu = 0
# while 循环执行
while x == "y":
    number = random.randint(1, 6)
    print("随机数", cishu, number)
    
    # if cishu == 3:
    #     # break 退出循环
    #     break

    cishu = cishu + 1


    if number == 1:
        print("===========")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("===========")

    if number == 2:
        print("===========")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print("===========")

    if number == 3:
        print("===========")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("===========")
        
    if number == 4:
        print("===========")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("===========")
        
    if number == 5:
        print("===========")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("===========")
        
    if number == 6:
        print("===========")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("===========")
    
    # 暂停 1 秒钟
    # time.sleep(1)

    x =  input("输入 y 重新摇骰子: ")

print("结束摇骰子")
