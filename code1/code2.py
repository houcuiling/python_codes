# 20240326
# 数学运算

# 加法例子
print("加法", (2 + 2))

# 减法例子
print("减法", (50 - 30))

# 乘法例子
print("乘法", (50 - 5 * 6))

# 除法例子
print("除法", ((50 - 5 * 6) / 4))

# float 浮点数 （小数）
xiaoshu = 8 / 5
print("浮点数", xiaoshu)

# 2, 4, 20 都是整数，类型: int
# 5.0, 1.6 都是浮点数，类型: float
# 除法运算 (/) 总是返回浮点数。

# floor diversion: 向下取整
print("17 / 3 =", (17 / 3))
print("17 // 3 =", (17 // 3))  # 向下取整为 5

# 取余 (%)
print("17 % 3 =", (17 % 3))

# 乘方 (**)
print("5的平方 =", 5**2)
print("2的7次方 =", 2**7)

width = 20  # 宽度
height = 5 * 9  # 高度
area = width * height  # 面积
width = 3  # 宽度
height = 4  # 高度

import math

length = math.sqrt(width * width + height * height)  # 对角线长度
print(length)

length = (width * width + height * height) ** 0.5
print(length)


########################### 文本 ###########################
# 20240327
# 文本的类型是 str, 是字符串(string)的英文缩写

# 1. 字符串乘法
print("------" * 4, "20240327", "------" * 4)  # 字符串也可以用乘法

# 2. 引号用法
boy_name = "lijianran"  # 双引号
girl_name = "houcuiling"  # 单引号 都可以，推荐你用双引号

print(boy_name, girl_name)

# 3. 换行字符
print("这是第一行...\n 这是，第二行...")  # '\n' 代表换行字符串

# 4. 转义字符
print("C:\some\name")  # '\n' 是转义字符，含义转换成了：换行
print(r"C:\some\name")  # 不换行，字符串前面加 r 表示使用原始字符串，不使用转义字符了

# 5. 多行字符
# 用三个引号包裹
# end="" 表示结尾不用回车，可以加上任意你想在末尾显示的字符串
print(
    """\
多了一个斜杠'\\'  没有回车
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""",
    end="",
)

print(
    """
没有这个斜杠'\\'  多了回车
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""",
    end="哈哈哈哈",
)

print()  # 输出空白字符，也会回车

# 6. 字符串加法
names = boy_name + " 和 " + girl_name
print(names)

# 7. 字符串长度
print(names, "的长度是", len(names))

# 8. 字符串 索引下标访问
word = "Python"
print(word, "长度是", len(word))
print("第0个字符是", word[0])
print("第1个字符是", word[1])
print("第2个字符是", word[2])
print("第3个字符是", word[3])
print("第4个字符是", word[4])
print("第5个字符是", word[5])
# print("没有第6个字符，这里会报错", word[6])

# 负数索引，表示从后往前
print("倒数第1个字符是", word[-1])
print("倒数第2个字符是", word[-2])
print("倒数第3个字符是", word[-3])
print("倒数第4个字符是", word[-4])
print("倒数第5个字符是", word[-5])
print("倒数第6个字符是", word[-6])
# 注意，-0 和 0 一样，因此，负数索引从 -1 开始。

# 9. 字符串切片
print(word[:2])
print(word[4:])
print(word[2:4])

### 这是小段注释
""" 这是大段注释
索引切片：
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

########################### 列表 ###########################
# 20240329
print("\n######### 列表 #########\n")

# 1. 列表啥都能放
liebiao = [1, 2, 3, 3213, 5]
print(liebiao)

zifuchuan_liebiao = ["P", "y", "t", "h", "on"]
print(zifuchuan_liebiao)

# 2. join 拼接函数
# 注意只能拼接字符串列表，数字或者其他列表不行
print(",".join(zifuchuan_liebiao))
print("-".join(zifuchuan_liebiao))
print(" ".join(zifuchuan_liebiao))
print("".join(zifuchuan_liebiao))
print(" haha ".join(zifuchuan_liebiao))

# 3. 列表切片
print(zifuchuan_liebiao[0])
print(liebiao[-2])

print(zifuchuan_liebiao[-3:])
print("".join(zifuchuan_liebiao[-3:]))

# 4. 列表合并
print(liebiao)
print(liebiao + [6, 7, 8])
liebiao.extend([6, 7, 8])  # extend 函数等价于 liebiao = liebiao + [6, 7, 8]
print("new_list", liebiao)

# 5. 修改列表
liebiao[3] = 4  # 修改 3213 为 4
print("new_list xiugai 1)", liebiao)

print(liebiao[2:5])
liebiao[2:5] = [5, 4, 3]  # 一次性切片修改三个值
print("new_list xiugai 2)", liebiao)

# 6. 列表新增
liebiao.append(9)  # 添加 9
print("new_list add 1)", liebiao)

liebiao.append(10)  # 添加 10
print("new_list add 2)", liebiao)

# 7. 常用
test_list = []

# 添加元素到列表
test_list.append(1.0)
test_list.append("test")
print(test_list)

# 拓展列表
test_list.extend([53])
print(test_list)

# 判断一个值是否在列表内
if "lijianran" in test_list:  # in 在里面
    print("find jianran")
else:
    test_list.append("lijianran")

# 计算某个值出现的次数
print("字符串 'lijianran' 出现的次数是", test_list.count("lijianran"))

# 某个元素的索引   从0开始算，第一次匹配到的位置
print("字符串 'test' 是列表中第几个：", test_list.index("test"))

# 删除元素
test_list.remove("lijianran")

# 列表元素个数 长度
print("test_list 的长度是", len(test_list))

# join 拼接字符串列表
test_list[0] = "1.0"
test_list[2] = "53"
print(test_list)
print("--这里随便写你想拼接在中间的字符串--".join(test_list))

# 反转列表
test_list.reverse()
print(test_list)
