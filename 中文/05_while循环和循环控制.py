# while循环

print("=== while循环演示 ===")
# 1. 基础while循环
a1 = 1
while a1 <= 5: #只要条件为真，代码就会重复执行，直到不成立为止
    print(f"计数:{a1}")
    a1 += 1  #相当于 a1 = a1 + 1，
    #当几次循环过后a1 = 6时，a1 <= 5为假，所以循环结束，也不会输出“计数：6”
    # 注意：不要忘记加条件，否则会无限循环！

# 2. 用户控制循环
print("\n=== 用户控制循环 ===")
TTL_EXP = 0.0
add = "yes"

while add.lower() == "yes":
    EXP = float(input("输入花费金额: "))
    TTL_EXP += EXP
    add = input("继续添加吗?(yes/no): ") 
    #如果输入yes，那么add.lower() == "yes"依旧成立，所以循环会继续；除非输入yes之外的任何内容，才会结束循环

print(f"总花费:{TTL_EXP}")

# 3.确保用户输入有效的pH值（0-14之间）
pH = float(input("请输入pH值(0-14): "))

while pH < 0 or pH > 14:
    print("错误:pH值必须在0-14之间!")
    pH = float(input("请重新输入pH值(0-14): "))

print(f"你输入的pH值 {pH} 是有效的")

# 3. break和continue
print("\n=== break和continue ===")
print("找到第一个能被3和5同时整除的数:")
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0: #i % 3 == 0指的是i处以3的余数等于0
        print(f"找到:{i}")   
        break  # 找到后就退出循环   
    i += 1

print("\n打印1-10的奇数:")
j = 1
while j <= 10:
    if j % 2 == 0:  # 如果是偶数
        j += 1      # 先递增
        continue     # 跳过剩余部分
    print(f"奇数:{j}")
    j += 1
