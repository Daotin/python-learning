"""
列表:是Python中最灵活的有序集合对象。它可以包含任意数量、任意类型的元素。
"""

# 创建包含整数的列表
numbers = [1, 2, 3, 4, 5]
print(f"整数列表: {numbers}")

# 创建包含不同类型元素的列表
mixed_list = ["apple", 123, True, 3.14]
print(f"混合类型列表: {mixed_list}")

# 列表可以嵌套
nested_list = [[1, 2], [3, 4]]
print(f"嵌套列表: {nested_list}")

"""
访问列表元素（索引与切片）
索引：正数索引从列表开头开始，负数索引从列表末尾开始。
切片：list[start:end:step]，end 不包含在内。
"""

my_list = ["a", "b", "c", "d", "e"]

# 访问第一个元素
print(f"第一个元素: {my_list[0]}")  # 输出: a

# 访问最后一个元素
print(f"最后一个元素: {my_list[-1]}")  # 输出: e

# 切片：获取前三个元素
print(f"前三个元素: {my_list[0:3]}")  # 输出: ['a', 'b', 'c']
print(f"前三个元素（简写）: {my_list[:3]}")  # 输出: ['a', 'b', 'c']

# 切片：从第二个元素到末尾
print(f"从第二个元素到末尾: {my_list[1:]}")  # 输出: ['b', 'c', 'd', 'e']

# 切片：每隔一个元素
print(f"每隔一个元素: {my_list[::2]}")  # 输出: ['a', 'c', 'e']

# 反转列表
print(f"反转列表: {my_list[::-1]}")  # 输出: ['e', 'd', 'c', 'b', 'a']

"""
修改列表元素（可变性）
"""
fruits = ["apple", "banana", "cherry"]
print(f"原始列表: {fruits}")

# 修改元素
fruits[1] = "orange"
print(f"修改后: {fruits}")  # 输出: ['apple', 'orange', 'cherry']

# 添加元素到末尾
fruits.append("grape")
print(f"添加元素后: {fruits}")  # 输出: ['apple', 'orange', 'cherry', 'grape']

# 插入元素到指定位置
fruits.insert(1, "kiwi")
print(f"插入元素后: {fruits}")  # 输出: ['apple', 'kiwi', 'orange', 'cherry', 'grape']

# 删除指定值的元素
fruits.remove("orange")
print(f"删除'orange'后: {fruits}")  # 输出: ['apple', 'kiwi', 'cherry', 'grape']

# 删除指定索引的元素并返回其值
popped_fruit = fruits.pop(0)
print(f"弹出'{popped_fruit}'后: {fruits}")  # 输出: ['kiwi', 'cherry', 'grape']

# 使用del关键字删除元素或切片
del fruits[1]
print(f"del删除后: {fruits}")  # 输出: ['kiwi', 'grape']

# 清空列表
fruits.clear()
print(f"清空后: {fruits}")  # 输出: []

print("-------------")


"""
元组是另一种序列数据类型，与列表非常相似，但它是不可变的（immutable）。这意味着一旦创建，元组中的元素就不能被修改、添加或删除。
"""

# 创建一个空元组
empty_tuple = ()
print(f"空元组: {empty_tuple}")

# 创建包含整数的元组
coordinates = (10, 20)
print(f"整数元组: {coordinates}")

# 创建包含不同类型元素的元组
mixed_tuple = ("hello", 123, False)
print(f"混合类型元组: {mixed_tuple}")

# 创建单元素元组时需要一个逗号，否则会被解释为普通表达式
single_element_tuple = (5,)
print(f"单元素元组: {single_element_tuple}, 类型: {type(single_element_tuple)}")
not_a_tuple = 5
print(
    f"不是元组: {not_a_tuple}, 类型: {type(not_a_tuple)}"
)  # 输出: 5, 类型: <class 'int'>

# 元组也可以嵌套
nested_tuple = ((1, 2), (3, 4))
print(f"嵌套元组: {nested_tuple}")

"""
访问元组元素（索引与切片）
元组的索引和切片操作与列表完全相同。
"""

"""
尝试修改元组元素会导致错误。
"""
point = (1, 2, 3)
# point[0] = 5  # 这行代码会引发 TypeError: 'tuple' object does not support item assignment

# 虽然元组本身不可变，但如果元组包含可变元素，这些可变元素内部是可以改变的
mutable_in_tuple = ([1, 2], "hello")
mutable_in_tuple[0].append(3)  # 这是合法的，因为我们修改的是列表内部，而不是元组本身
print(f"包含可变元素的元组: {mutable_in_tuple}")  # 输出: ([1, 2, 3], 'hello')


"""
综合比较

| 特性 | 列表（List） | 元组（Tuple） |
| --- | --- | --- |
| 语法 | [] 方括号 | () 圆括号 |
| 可变性 | 可变（mutable）：可以添加、删除、修改元素 | 不可变（immutable）：一旦创建不能修改 |
| 性能 | 相对元组，操作速度稍慢，占用内存稍多 | 相对列表，操作速度稍快，占用内存稍少 |
| 用途 | 元素集合需要频繁变更，如动态数据 | 元素集合固定不变，如坐标、数据库记录等 |
| 典型场景 | 存储数据集、操作动态数组 | 函数返回多个值、字典的键（元组可哈希） |
"""


"""
作业
"""
# 任务1: 学生成绩列表操作
# 你有一个学生在不同科目上的成绩列表。请完成以下操作：
scores = [85, 90, 78, 92, 88]
print(f"原始成绩列表: {scores}")

# TODO 1.1: 将第一门科目的成绩改为 95
scores[0] = 95
# TODO 1.2: 添加一门新科目的成绩 93 到列表末尾
scores.append(93)
# TODO 1.3: 删除最低分 (假设最低分是 78)，可以使用 remove() 或 pop() 并找到索引
scores.remove(78)

print(f"修改后的成绩列表: {scores}")

# 任务2: 学生信息元组操作
# 你有一个学生的不可变信息元组 (姓名, 年龄, 性别)。
student_info = ("张三", 20, "男")
print(f"学生信息元组: {student_info}")

# TODO 2.1: 尝试将学生的年龄修改为 21。观察会发生什么？请在代码中注释说明。
# student_info[1] = 21 # 尝试修改这里

# TODO 2.2: 访问并打印学生的姓名和年龄。
