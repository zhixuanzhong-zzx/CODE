user_name = input("请输入你的名字：")
balance = 500000

def search(switch):
    if switch: #函数的参数能当一个开关使用，控制调用时是否出现这句话
        print("--------查询余额--------")
    print(f"{user_name}，你好，您的余额剩余：{balance}元")
def add(addmoney):
    print(f"您存款{addmoney}成功")
    global balance
    balance += addmoney
def substract(substractmoney):
    print(f"您取款{substractmoney}成功")
    global balance
    balance -= substractmoney
def menu():
    print("--------主菜单--------\n"
    f"{user_name}，您好，这是ATM，请选择操作：\n"
    "查询余额\t【输入1】\n"
    "存款\t\t【输入2】\n"
    "取款\t\t【输入3】\n"
    "退出\t\t【输入4】"
    )
    return input("请输入你的选择：") #return的结果可以和上面函数体一点关联都没有

while True:
    x = menu()   
    if x == "1":
        search(True)
    elif x == "2":
        addmoney = int(input("您想存入："))
        add(addmoney)
        search(False)
    elif x == "3":
        substractmoney = int(input("您想取出："))
        substract(substractmoney)
        search(False)
    else:
        print("现在退出")
        break

'''
这边第24行的返回值设置、27行的赋值相当于
x = input("请输入你的选择：")、menu()（不加返回值设置）
现在这样相当于input函数提前写在return后面
'''