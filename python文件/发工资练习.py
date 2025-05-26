s = 10000
for i in range(1,21):
    import random
    num = random.randint(1,11)
    if num >= 5:
        s -= 1000
        print(f"员工{i}，发工资1000块，账户余额{s}")
    else:
        print(f"员工{i}，绩效分数{num}，下一位")
        continue
    if s == 0:
        print("发完了，走吧孩子")
        break