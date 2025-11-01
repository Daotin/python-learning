"""
代码块：是当条件满足时要执行的语句集合。Python 使用缩进（通常是4个空格）来表示代码块的归属。这是Python语法中非常重要且独特的地方，务必保持一致的缩进。

缩进是关键：Python 不使用大括号来定义代码块，而是使用缩进。错误的缩进会导致 IndentationError 或逻辑错误。
"""

# if
age = 18
if age >= 20:
    print("你已成年。")
print("程序继续执行。")


# if else
score = 75
if score >= 80:
    print("考试及格！")
else:
    print("考试不及格，请继续努力！")

# if elif else
temperature = 18
if temperature > 30:
    print("天气很热，注意防暑。")
elif temperature > 20:
    print("天气适中，很舒服。")
elif temperature > 10:
    print("天气凉爽，可以加件薄外套。")
else:
    print("天气寒冷，请多穿衣服。")

# 组合条件和嵌套
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("欢迎入场！")
elif age < 18 and has_ticket:
    print("抱歉，未成年人禁止入场。")
else:
    print("请先购买门票。")

# 条件语句也可以进行嵌套
is_member = True
purchases_amount = 120

if is_member:
    if purchases_amount > 100:
        print("尊敬的会员，您享受大额消费折扣！")
    else:
        print("尊敬的会员，欢迎光临！")
else:
    print("欢迎新顾客！注册会员可享受更多优惠。")


"""
练习
"""
# 获取用户输入，并将其转换为整数
# 提示：input() 函数默认返回字符串，需要用 int() 进行转换
num_str = input("请输入一个整数：")
num = int(num_str)

# 在这里添加你的条件判断逻辑
# 使用 if-elif-else 结构来判断 num 是正数、负数还是零

# 例如：
if num > 0:
    print("这是一个正数")
elif num < 0:
    print("这是一个负数")
else:
    print("这是0")
