import random
num = random.randint(1,10)
x = int(input("请输入："))

if x == num:
    print("nb，对了")
else:
    if x > num:
        print("大了") 
    elif x < num:
        print("小了")
    y = int(input("请再次输入："))
    if y == num:
        print("好，对了")
    else:
        if y > num:
            print("大了") 
        elif y < num:
            print("小了")
        z = int(input("请最后一次输入："))
        if z == num:
            print("好，对了")
        else:
            if z > num:
                print(f"大了，是{num}") 
            elif z < num:
                print(f"小了，是{num}")
'''
可以不用新的变量名y、z
可以重复对一个变量赋新值:
num = int(input("再次输入你的猜测："))
'''