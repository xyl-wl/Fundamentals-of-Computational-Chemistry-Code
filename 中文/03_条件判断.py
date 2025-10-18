# 条件判断

print("=== 条件判断演示 ===")

# 1. 基础if语句
temp = 36.8

if temp > 37.5: #本条件为真时，执行
    print(f"当前体温是{temp}°C,体温偏高，建议休息")
elif temp < 36.0: #前面的条件为假，本条件为真时，执行
    print(f"当前体温是{temp}°C,体温偏低，注意保暖")
else: #前面所有条件都为假时，执行
    print(f"当前体温是{temp}°C,体温正常")

# 2. 逻辑运算符 and, or, not
print("\n=== 逻辑运算符——and ===")
age = 25
license = True
if age >= 18 and license:
    print("可以开车")  # 两个条件都满足时，执行
else:
    print("不能开车")

print("\n=== 逻辑运算符——or ===")
#假如你有一个电子密码门锁，不管是用钥匙还是输入密码都可以打开
pw = 654987
key = True
if pw or key: 
    print("开锁成功") #当两个条件有一个满足时，执行
else:
    print("开锁失败")

print("\n=== 逻辑运算符——not ===")
# 空字符串
name = ""  
if not name:  # 等效于if not bool(name): 本质上not只处理布尔值，但Python会将变量自动转换成布尔值
    print("姓名不能为空！")  # 会执行这个，因为not False = True
else:
    print(f"你好，{name}")


# 3. 嵌套if语句
print("\n=== 实验室试剂整理分类系统===")

while True: #这是一个不遇见break就会一直运行的循环
    try:
        type_1 = input("请输入试剂类型(solid/liquid): ").lower()

        if type_1 == "solid":
            weight = int(input("试剂的重量是多少(g): "))
            if weight >= 500:
                print("请其放在固体试剂仓库。")
            else:
                print("请将其放在实验室的固体试剂柜中。")
            break  # 退出循环
            
        elif type_1 == "liquid":
            volume = int(input("试剂的体积是多少(ml): "))
            if volume >= 500:
                print("请将其放在液体试剂仓库。")
            else:
                print("请将其放在实验室的液体试剂柜中。")
            break  # 退出循环
            
        else:
            print("错误：请输入'solid'或'liquid'")
            # 这里不加break，可以重新开始继续循环，重新输入
            
    except ValueError: 
        print("错误：请输入有效的数字！")
        # 同样不break，继续循环，重新输入
    
    except KeyboardInterrupt:
        print("\n用户取消操作")
        break
        
    except Exception as e:
        print(f"发生未知错误: {e}")
        print(f"异常类型: {type(e).__name__}")
        break # 如果担心这个位置错误是严重错误，就加break退出循环
    
print("程序执行完毕")
