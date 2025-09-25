# loops_for.py - for循环

# 1. 遍历列表
print("\n=== 遍历列表 ===")
drugs = ["阿司匹林", "胰岛素", "抗生素", "维生素C"]
print("药品清单:")
for drug in drugs:#遍历在drugs中的每一个元素，并用drug来指代他们
    print("- " + drug) #注意缩进，否则会报错

# 2.还可以遍历字符串的每一个字符
print("\n=== 遍历字符 ===")
dna_sequence = "ATCG"
for base in dna_sequence:
    print(f"Found nucleotide: {base}")

# 3. 基础range循环
print("打印0-4:")
for i in range(5):  # 0,1,2,3,4
    print("当前数字:", i)

print("\n打印1-5:")
for i in range(1, 6):  # 1,2,3,4,5
    print("当前数字:", i)

print("\n打印1-10的奇数:")
for i in range(1, 11, 2):  # 1,3,5,7,9，步长为2
    print("奇数:", i)


# 4. 实际应用：计算总和
print("\n=== 计算1-100的和 ===")
total = 0
for number in range(1, 101):
    total += number  # 等同于 total = total + number

print("1到100的和是:", total)

# 5. 嵌套循环 - 乘法表
print("\n=== 简易乘法表 ===")
for i in range(1, 4):  # 1,2,3
    for j in range(1, 4):  # 1,2,3
        print(f"{i} × {j} = {i * j}", end="  ") #结束后加两个空格
    print()  # 换行
    
    
    
    


