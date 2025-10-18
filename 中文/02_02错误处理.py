# 错误处理
# 当用户输入的内容有问题时，程序会崩溃，所以需要用到错误处理来避免

try: # 尝试执行的代码
    a = int(input("请输入一个数字: "))
    b = 10 / a
    print(f"结果是: {b}")
    
except ValueError: # 处理输入非数字的情况
    print("错误：请输入有效的数字！")
    
except ZeroDivisionError: # 处理输入0时的除零错误
    print("错误：不能输入0！")
    
except Exception as e: # 处理其他未知异常，e是一个变量，用来存储捕获到的异常
    #除了SystemExit(程序退出)、KeyboardInterrupt(用户按 Ctrl+C)、GeneratorExit(生成器关闭)无法捕捉，其余的大多数异常可以被捕捉到
    print(f"发生未知错误: {e}")
    print(f"异常类型: {type(e).__name__}") # 打印异常的类型名称

else: # 如果没有发生错误，执行这里的代码
    print("计算成功！")
    
finally: # 无论是否发生错误，都会执行这里的代码
    print("程序执行完毕")
    
#以上就是一个简单又完整的错误处理结构