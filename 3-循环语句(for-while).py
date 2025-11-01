"""
for 循环用于遍历任何可迭代对象（如列表、元组、字符串、字典、集合以及range()函数生成的序列）。它会依次取出可迭代对象中的每一个元素，并执行相应的代码块。

range() 函数是一个常用的序列生成器，它能生成一系列数字。常与for循环结合使用来执行特定次数的循环。

range(stop): 生成从0到stop-1的整数序列。
range(start, stop): 生成从start到stop-1的整数序列。
range(start, stop, step): 生成从start到stop-1，步长为step的整数序列。
"""

# 循环5次，打印从0到4的数字
print("使用 range(5):")
for i in range(5):
    print(i)

# 循环打印从2到5的数字
print("\n使用 range(2, 6):")
for i in range(2, 6):
    print(i)

# 循环打印从0到9的偶数
print("\n使用 range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("\n遍历列表:")
for fruit in fruits:
    print(fruit)

# 遍历字符串
word = "Python"
print("\n遍历字符串:")
for char in word:
    print(char)

# 遍历字典的键
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\n遍历字典的键:")
for key in person:
    print(f"key: {key}, value: {person[key]}")

# 遍历字典的值
print("\n遍历字典的值:")
for value in person.values():
    print(value)

# 遍历字典的键值对
print("\n遍历字典的键值对:")
for key, value in person.items():
    print(f"{key}: {value}")


"""
break 和 continue 语句
"""
print("使用 break:")
for i in range(10):
    if i == 5:
        break  # 当 i 等于 5 时，停止循环
    print(i)

print("\n使用 continue:")
for i in range(10):
    if i % 2 == 0:  # 如果是偶数，跳过本次循环的print语句
        continue
    print(i)  # 只会打印奇数


"""
while 循环
"""
# 使用 while 循环计算从1到5的和
count = 1
sum_val = 0
print("使用 while 循环计算和:")
while count <= 5:
    sum_val += count
    count += 1  # 每次循环后增加 count 的值，否则会无限循环
print(f"1到5的和是: {sum_val}")

# while 循环结合 break
secret_number = 7
guess = 0
print("\n猜数字游戏 (while + break):")
while True:  # 无限循环，直到条件满足手动break
    guess = int(input("请输入一个数字 (0-9): "))
    if guess == secret_number:
        print("恭喜你，猜对了!")
        break
    else:
        print("猜错了，再试一次。")


"""
作业
"""


# 任务1：使用 for 循环计算一个数的阶乘
# 阶乘的定义：n! = n * (n-1) * ... * 1
def calculate_factorial(n):
    # 初始化结果为1
    factorial = 1
    # 使用 for 循环，从1遍历到n，并将每个数乘到 factorial 中
    # range(1, n + 1) 会生成从1到n的序列
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


# 任务2：使用 while 循环倒序打印列表中的所有元素
def reverse_print_list(data_list):
    # 初始化一个索引，使其指向列表的最后一个元素
    # 列表的长度可以通过 len() 函数获取
    # 列表的最后一个元素的索引是 len(data_list) - 1
    # 使用 while 循环，当索引有效时，打印当前索引处的元素，并递减索引
    last_index = len(data_list) - 1
    while last_index >= 0:
        print(data_list[last_index])
        last_index -= 1


# 测试任务1
number = 5
print(f"{number}! = {calculate_factorial(number)}")  # 预期输出: 5! = 120

# 测试任务2
my_list = [10, 20, 30, 40, 50]
print("\n倒序打印列表:")
reverse_print_list(my_list)  # 预期输出: 50 40 30 20 10 (每行一个或空格分隔)
