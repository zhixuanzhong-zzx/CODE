i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print(f"{sum}")


import random
num = random.randint(1,100)
a = int(input("猜猜看呐："))
times = 1

while a != num:
    if a > num:
        print("大了")
    else:
        print("小了")
    times += 1
    a = int(input(f"试第{times}次："))
print(f"恭喜就是{num}")


#也可以这样写，直接用一个布尔类型
flag = True
count = 0  
import random
num2 = random.randint(1,100)

while flag:
    guess_num = int(input("请输入你猜测的数字:"))
    count += 1
    if guess_num == num2:
        print("猜中了")
        flag = False  # 终止循环
    else:
        if guess_num > num2:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"你总共猜测了{count}次")