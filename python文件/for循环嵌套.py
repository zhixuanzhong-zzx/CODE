
for x in range(1,101):
    y = 1
    for y in range(1,11):
        print(f"送你今天第{y}朵花")
    print("小美我爱你")
print(f"第{x}表白成功")

'''
嵌套循环的两个临时变量需要不同字母
'''

for i in range(1,10):
    j = 1
    for j in range(1,i + 1):
        print(f"{j}*{i}={j*i}\t", end="")
    print("")

"""
相比于while循环，不用设置j += 1的步进器
"""