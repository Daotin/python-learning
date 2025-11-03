"""
字典：类似js中的对象，是一种键值对（key-value）存储的数据结构。
1、创建字典使用花括号 {}，键值对之间用冒号 : 分隔，多个键值对用逗号 , 分隔。
2、访问字典中的值通过键来获取，使用方括号 [] 或 get() 方法。
3、字典是可变的，可以添加、修改和删除键值对。
"""

# 创建一个空字典
empty_dict = {}
print(f"空字典: {empty_dict}")

# 创建一个包含数据的字典
student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": {"math": 95, "physics": 88},
}
print(f"学生信息字典: {student_info}")

# 也可以使用 dict() 构造函数
another_dict = dict(brand="Ford", model="Mustang", year=1964)
print(f"另一个字典: {another_dict}")


"""
访问字典元素
1、不能使用点号（.）来访问字典的值，因为字典不是对象。
2、使用方括号 [] 访问字典中的值时，如果键不存在会引发 KeyError。
3、使用 get() 方法访问字典中的值时，如果键不存在会返回 None。
"""

print("--------------------")

print(f"Alice 的年龄: {student_info['age']}")
# print(f"Alice 的年龄: {student_info.age}")
print(
    f"Alice 的专业: {student_info.get('major')}"
)  # 使用 .get() 方法，如果键不存在则返回 None，不会报错

# 尝试访问不存在的键
# print(student_info['city']) # 这会引发 KeyError
print(f"Alice 的城市: {student_info.get('city', '未知111')}")  # 可以提供一个默认值

"""
增删改查字典元素
1、添加或修改键值对：使用赋值语句 dict[key] = value
2、删除键值对：使用 del 语句或 pop() 方法（pop() 方法删除不存在的键时不会报错，但是需要提供默认值）
3、查询字典长度：使用 len() 函数
4、清空字典：使用 clear() 方法
"""

print("--------------------")

# 添加新元素
student_info["city"] = "New York"
print(f"添加城市后的字典: {student_info}")

# 修改元素
student_info["age"] = 21
print(f"修改年龄后的字典: {student_info}")

# 删除元素
del student_info["major"]
print(f"删除专业后的字典: {student_info}")

# del student_info["city1"]  # 尝试删除不存在的键会引发 KeyError
# 安全删除
student_info.pop("city1", None)  # 如果键不存在则返回 None，不会报错
print(f"删除城市后的字典: {student_info}")

# 使用 pop() 删除并返回被删除的值
grades = student_info.pop("grades")
print(f"删除成绩后的字典: {student_info}, 被删除的成绩: {grades}")

# 查询字典长度
length = len(student_info)
print(f"字典长度: {length}")

# 清空字典
student_info.clear()
print(f"清空后的字典: {student_info}")


"""
字典的常用方法
1、keys(): 返回字典中所有的键
2、values(): 返回字典中所有的值
3、items(): 返回字典中所有的键值对
"""
print("--------------------")
product = {"name": "Laptop", "price": 1200, "quantity": 50}

print(f"所有键: {product.keys()}")
print(f"所有值: {product.values()}")
print(f"所有键值对: {product.items()}")

# 遍历字典
print("遍历字典的键:")
for key in product.keys():
    print(key)

print("遍历字典的值:")
for value in product.values():
    print(value)

print("遍历字典的键值对:")
for key, value in product.items():
    print(f"{key}: {value}")


"""
集合：集合是一种无序的、不重复元素的数据结构。它支持数学上的集合运算，如并集、交集、差集等。集合中的元素必须是不可变类型（例如数字、字符串、元组），列表和字典不能作为集合的元素。

创建： 使用花括号 {} 或 set() 函数创建集合。元素之间用逗号 , 分隔。
    使用set，参数可以是一个可迭代对象（如列表、元组，字典/字典的键）。

注意：列表和字典不能作为集合的元素。
"""

print("--------------------")

# 创建一个空集合
empty_set = set()
print(f"空集合: {empty_set}")

# 创建一个包含数据的集合 (重复元素会被自动移除)
numbers = {1, 2, 3, 3, 4, 5, 5, 1}
print(f"数字集合: {numbers}")

# 从列表创建集合
my_list = [10, 20, 30, 20, 40]
my_set = set(my_list)
print(f"从列表创建的集合: {my_set}")


# aaa = {[1, 2, 3], [4, 5, 6]}  # 错误示范，列表不可哈希，不能作为集合元素
# 正确示范，使用元组作为集合元素
bbb = {(1, 2, 3), (4, 5, 6)}
print(f"使用元组作为集合元素: {bbb}")


"""
集合的增删改查
1、添加元素：使用 add() 方法添加单个元素，使用 update() 方法添加
2、删除元素：使用 remove() 方法删除指定元素（不存在会报错），使用 discard() 方法删除指定元素（不存在不会报错），使用 pop() 方法随机删除一个元素
3、查询集合长度：使用 len() 函数
4、清空集合：使用 clear() 方法
"""
print("--------------------")
fruits = {"apple", "banana"}
fruits.add("orange")
print(f"添加元素后的集合: {fruits}")

fruits.remove("banana")
print(f"移除 'banana' 后的集合: {fruits}")

fruits.discard("grape")  # 'grape' 不在集合中，不会报错
print(f"尝试移除 'grape' 后的集合 (使用 discard): {fruits}")

# fruits.remove("grape") # 这会引发 KeyError

fruits.clear()
print(f"清空后的集合: {fruits}")

"""
集合运算
1、并集 (union): 使用 union() 方法或 | 运算符
2、交集 (intersection): 使用 intersection() 方法或 & 运算符
3、差集 (difference): 使用 difference() 方法或 - 运算符
4、对称差集 (symmetric difference): 使用 symmetric_difference() 方法或 ^ 运算符
5、子集与超集: 使用 issubset() 和 issuperset() 方法
"""
print("--------------------")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 并集 (union): 包含两个集合的所有元素
union_set = set_a.union(set_b)  # 或者 set_a | set_b
print(f"并集: {union_set}")

# 交集 (intersection): 包含两个集合共有的元素
intersection_set = set_a.intersection(set_b)  # 或者 set_a & set_b
print(f"交集: {intersection_set}")

# 差集 (difference): 包含在第一个集合中但不在第二个集合中的元素
difference_set = set_a.difference(set_b)  # 或者 set_a - set_b
print(f"A - B 的差集: {difference_set}")

difference_set_b_a = set_b.difference(set_a)  # 或者 set_b - set_a
print(f"B - A 的差集: {difference_set_b_a}")

# 对称差集 (symmetric difference): 包含在任一集合中但不同时在两个集合中的元素
symmetric_difference_set = set_a.symmetric_difference(set_b)  # 或者 set_a ^ set_b
print(f"对称差集: {symmetric_difference_set}")

# 子集与超集
set_c = {1, 2}
print(f"set_c 是 set_a 的子集吗? {set_c.issubset(set_a)}")  # 或者 set_c <= set_a
print(f"set_a 是 set_c 的超集吗? {set_a.issuperset(set_c)}")  # 或者 set_a >= set_c


"""
字典，集合的应用场景
1、字典适用于需要通过唯一键快速查找、插入和删除数据的场景，如用户信息存储、配置参数管理等。
2、集合适用于需要存储唯一元素并进行集合运算的场景，如标签管理、权限控制等。

字典，集合的增删改查总结：
| 操作类型 | 字典 (Dictionary)               | 集合 (Set)                     |
|----------|--------------------------------|--------------------------------|
| 创建     | 使用 {} 或 dict()               | 使用 {} 或 set()                |
| 访问     | 通过键访问 dict[key] 或 dict.get(key) | 不适用（集合无键值对）        |
| 添加     | dict[key] = value               | set.add(element) 或 set.update(iterable) |
| 删除     | del dict[key] 或 dict.pop(key) | set.remove(element) 或 set.discard(element) 或 set.pop() |
| 修改     | dict[key] = new_value           | 不适用（集合元素不可修改）    |
| 查询长度 | len(dict)                       | len(set)                       |
"""


"""
作业
"""

# 客户原始数据列表，每个客户是一个字典
all_customers_data = [
    {"id": "C001", "name": "张三", "email": "zhangsan@example.com", "status": "active"},
    {"id": "C002", "name": "李四", "email": "lisi@example.com", "status": "inactive"},
    {"id": "C003", "name": "王五", "email": "wangwu@example.com", "status": "active"},
    {"id": "C004", "name": "赵六", "email": "zhaoliu@example.com", "status": "active"},
    {"id": "C005", "name": "钱七", "email": "qianqi@example.com", "status": "inactive"},
]

# 本月活跃的客户ID列表（可能包含新注册的客户）
monthly_active_ids = ["C001", "C003", "C004", "C006", "C007"]

# --- 你的代码从这里开始 ---

# 1. 创建一个字典 `customer_lookup`，将客户ID映射到完整的客户信息字典
#    例如: {"C001": {"id": "C001", ...}, ...}
customer_lookup = {}
# 遍历 all_customers_data 列表，填充 customer_lookup 字典
for customer in all_customers_data:
    customer_lookup[customer["id"]] = customer

print(f"\n客户查找字典: {customer_lookup}")

# 2. 创建一个集合 `all_customer_ids`，包含所有客户的ID
all_customer_ids = set()
# 遍历 customer_lookup 字典的键，填充 all_customer_ids 集合
for customer_id in customer_lookup.keys():
    all_customer_ids.add(customer_id)

print(f"\n所有客户ID集合: {all_customer_ids}")
print(f"\n所有客户ID集合1: {set(customer_lookup.keys())}")
print(f"\n所有客户ID集合2: {set(customer_lookup)}")

# 3. 创建一个集合 `active_customer_ids`，包含本月活跃客户的ID
active_customer_ids = set(monthly_active_ids)

print(f"\n本月活跃客户ID集合: {active_customer_ids}")

# 4. 使用集合操作找出当月新增的活跃客户ID
#    提示：新增活跃客户是指那些在本月活跃，但不在所有客户ID集合中的客户
new_active_customers = set()
new_active_customers = active_customer_ids.difference(all_customer_ids)
print(f"\n当月新增活跃客户ID: {new_active_customers}")

# 5. 使用集合操作找出当月不活跃的老客户ID
#    提示：不活跃老客户是指那些在所有客户ID集合中，但不在本月活跃客户ID集合中的客户
inactive_old_customers = set()
inactive_old_customers = all_customer_ids.difference(active_customer_ids)

print(f"\n当月不活跃老客户ID: {inactive_old_customers}")


print("\n--- 作业结束 ---\n")


print(f"{set({1: 222, 2: 333})}")  # 输出: {1, 2}
