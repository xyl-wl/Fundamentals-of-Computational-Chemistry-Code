# 用户输入和类型转换
# 注意：input()永远返回字符串，数学计算需要先转换类型。
print("=== 用户交互演示 ===")

# 1. 基本输入
name = input("请输入你的名字: ")
print(f"你好,{name}!")

# 2. 数字输入（需要类型转换）
print("\n=== 数字计算 ===")
# 错误示范：input()返回的是字符串
a1 = input("请输入第一个数字: ")
a2 = input("请输入第二个数字: ")
print(f"a1 + a2 = {a1 + a2}(错误示范-没有转换数据类型)")  # 这是字符串连接，不是数学加法！
# 正确示范：转换为数字
a1_f = float(a1)  # 转换为浮点数
a2_f = float(a2)
print(f"a1 + a2 = {a1_f + a2_f}(正确转换数据类型)")

# 3. 在输入时直接转换
age = int(input("请输入你的年龄: "))
print(f"明年你就{age + 1}岁了")

# 4. 实际应用：BMI计算
print("\n=== BMI计算器 ===")
height = float(input("请输入身高(米): "))
weight = float(input("请输入体重(公斤): "))
bmi = weight / (height ** 2)
print(f"你的BMI指数是: {bmi:.2f}")

# 5.一次获取多个输入
# 方法1：分开获取
print("\n=== 分开获取多个输入 ===")
print("请输入三个整数：")
a = int(input("第一个整数："))
b = int(input("第二个整数："))
c = int(input("第三个整数："))
print(f"您刚才输入的三个数字分别是{a},{b},{c}")

# 方法2：一次输入，用空格分隔
print("\n=== 一次输入，用空格分隔 ===")
a_three = input("请输入三个整数，用空格分隔：")
numbers = a_three.split()  # split() 按空格分割字符串，并返回到名为numbers的列表
a, b, c = int(numbers[0]), int(numbers[1]), int(numbers[2]) #字符串转换成整数
print(f"您刚才输入的三个整数分别是{a},{b},{c}")



