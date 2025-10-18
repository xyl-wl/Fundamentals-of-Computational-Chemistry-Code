# 变量和数据类型.py - 常用变量和数据类型

print("=== 变量和数据类型 ===")

# 1. 基础变量类型
name = "张三"  # 字符串(文本)
age = 22       # 整数
height = 1.75  # 浮点数(小数)
degree = True  # 布尔值(True/False)

print(f"姓名:{name}")
print(f"年龄:{age}岁")
print(f"身高:{height}米")
print(f"学位:{degree}")

# (1)布尔值
print("\n=== 布尔值 - True/False ===") #\n是换行符
# 空字符串、0、None等会转为False，其他转为True
print(bool(""),bool(()),bool({}),bool([])) 
# 空序列，比如空字符串、空元组、空字典、空列表，结果为False
print(bool(None))    # None，结果为False
print(bool("None"))  # 注意：这里的"None"是字符串，所以是True
print(bool("Hello")) # 非空字符串，结果为True
print(bool("False")) # 非空字符串，结果为True
print(bool(0))       # 0，结果为False  
print(bool(1))       # 1（非0），结果为True

# (2)浮点数
print("\n=== 浮点数的小数位保留 ===")
pi = 3.1415926535
a = 5 #小数点后保留的位数
print(f"保留{a}位小数的π={pi:.5f}(第一种写法)") #:.5f表示浮点精度，其中的数字表示小数位数 (比如':.3f' 表示保留三位小数)
print(f"保留{a}位小数的π={pi:.{a}f}(第二种写法)") #python版本高的可以这样写
print(f"保留{a}位小数的π={round(pi,5)}(第三种写法)") #还可以用round函数，语法是round（变量名，保留的位数）
print("保留{}位小数的π={}(第四种写法)".format(a,round(pi, a)))
print("保留{}位小数的π={:.5f}(第五种写法)".format(a,pi)) 
# 注意：以上的pi的实际值依旧是3.1415926535，它只是显示为3.14159

#所以当你需要一个保留了5位小数的pi的变量时
pi_5 = round(pi,5) 
print(f"保留{a}位小数的π={pi_5:.{a}f}(使用round函数)")

# 2. 查看数据类型
print("\n=== 数据类型检查 ===")
print(f"name的类型:{type(name)}")
print(f"age的类型:{type(age)}")
print(f"height的类型:{type(height)}")
print(f"degree的类型:{type(degree)}")

# 3. 变量重新赋值
print("\n=== 变量重新赋值 ===")
b = 10
print(f"初始值:{b}")
b = b + 5  # 重新赋值
print(f"加5后:{b}")

# 4. 多个变量赋值
print("\n=== 多个变量赋值 ===")
x, y, z = 1, 2, 3
print(f"x = {x},y = {y},z = {z}")
