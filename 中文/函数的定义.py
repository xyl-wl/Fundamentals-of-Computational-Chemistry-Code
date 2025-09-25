#开始定义一个新的函数

def calculate_gc_content(dna_sequence): 
    """
    计算给定DNA序列字符串的GC含量（百分比）。
    这个函数可以省略重复代码来批量处理多个DNA序列。
    'calculate_gc_content' 是此函数的自定义名称。
    'dna_sequence'是参数名，表示调用函数时的输入DNA字符串。
    """
    # 1. 将序列全部转换为大写。
    # 避免结果出现错误，因为在计算机语言中中'g'和'G'是不同的字符。
    sequence = dna_sequence.upper() 

    # 2. 统计序列中“G”和“C”核苷酸的数量。
    g_count = sequence.count('G') #统计“G”的数量
    c_count = sequence.count('C') #同上
    total_length = len(sequence) #计算序列的总长度。注意：它的计算会包含任何其他字符（如果有空格、换行符的话）。

    # 3. 避免序列为空时出现的除零错误。
    if total_length == 0:
        return 0.0

    # 4. 计算GC含量并以百分比形式返回。
    gc_content = (g_count + c_count) / total_length * 100

    # 5. 返回结果
    return gc_content

abc = "ATCG"
result = calculate_gc_content(abc) # 将变量abc输入到前面定义好的函数
print(result) # 结果是50.0
print(f"The GC content of {abc} is {result:.2f}%") 
#:.2f表示浮点精度，其中的数字表示小数位数 (比如':.3f' 表示保留三位小数)
#Note: 注意：`result`的实际值依旧是50.0，它只是显示为50.00

print("=" * 60)#另一种打印形式
print("The GC content of ATCG is {:.2f}%".format(result)) 
print("The GC content of ATCG is {}%".format(result)) 

print("=" * 60)#不要忘了f，这是有f和没有的区别
print(f"The GC content of {abc} is {result}%") 
print("The GC content of {abc} is {result}%") 

print("=" * 60)
#当你需要一个新的保留了几位小数的数字，可以用round函数
result = 50.123124
print("The GC content is {:.2f}%".format(result)) 
print(result) #输出50.123124，因为:.2f只更改变量在打印时的显示，其余什么也不变
round1 = round(result, 4) #新定义一个变量来储存保留小数的数字
#round函数的语法是round(变量, 想保留的小数位数)
print(round1)

