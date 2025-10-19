#函数的定义

# 1. 无参数无返回值的函数
def greet():   #简单的问候函数
    print("你好！很高兴认识你！")

greet() # 调用函数

# 2. 带参数的函数
def greet_name(name):  #name就是自定义的参数名字
    print(f"你好，{name}！很高兴认识你！")

greet_name("Lily") # 调用函数

# 3. 带参数和返回值的函数:计算给定DNA序列字符串的GC含量（百分比）。
def content(dna): 
    # 1. 将序列全部转换为大写。
    seq = dna.upper() 

    # 2. 统计序列中“G”和“C”核苷酸的数量。
    g = seq.count('G') #统计“G”的数量
    c = seq.count('C') #同理
    length = len(seq) #计算序列的总长度。注意：它的计算会包含任何其他字符。

    # 3. 避免序列为空时出现的除零错误。
    if length == 0:
        return 0.0

    # 4. 计算GC含量并以百分比形式返回。
    g_c = (g + c) / length * 100

    # 5. 返回结果
    return g_c

abc = "ATCG"
dd = ""
result1 = content(abc) # 调用函数
result2 = content(dd)
print(f"The GC content of {abc} is {result1:.2f}%") 
print(f"The GC content of {dd} is {result2:.2f}%") 

# 4. 多个返回值
def circle(R):
    #计算圆的面积和周长
    S = 3.14159 * R ** 2
    C = 2 * 3.14159 * R
    return S, C  # 返回元组(是一种不可变的序列类型)

# 接收多个返回值
A = 5
a1, a2 = circle(A)
print(f"半径为{A}的圆: 面积={a1:.2f}, 周长={a2:.2f}")
