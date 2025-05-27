user_name = input("请输入你的姓名：")
balance = 5000000
x = 0
def menu():
    print("----------主菜单----------")
    global x
    x  = int(input(
        f"{user_name}，您好，这是ATM，请选择操作：\n"
        "查询余额\t【输入1】\n"
        "存款\t\t【输入2】\n"
        "取款\t\t【输入3】\n"
        "退出\t\t【输入4】\n"
        "请输入您的选择："
    ))
def search():
    print("----------查询余额----------")
    print(f"{user_name}，您好，您的余额余：{balance}元")
def add():
    print("----------存款----------")
    addmomey = int(input("您想要存款的金额为："))
    global balance
    balance += addmomey
    print(f"存款成功，目前余额为：{balance}元")
def subtract():
    print("----------取款----------")
    subtractmoney = int(input("您想要取出的金额为："))
    global balance
    balance -= subtractmoney

while True:
    menu()
    if x == 1:
        search()
        continue
    elif x == 2:
        add()
        continue
    elif x== 3:
        subtract()
        continue
    elif x == 4:
        print("现在退出")
        break
    else:
        print("输入错误，退出")
        break
'''
1、全局变量必须在函数体外先申明一下，    print(f"取款成功，目前余额为：{balance}元")
单独在函数体中gobal x一下没用，不算，会报错
2、下面x == 1，需要x是一个数字数据类型，
包括下面addmoney后面要做加法，也需要是数字数据类型
3、菜单那里四个选项一开始没有对齐，每一行添加了一个制表符后就对齐了
4、一开始菜单函数那里input中的内容用的是三个引号"""保留其中的换行和缩进格式，
但是这部分内容在终端上会往右偏等等位置显示问题，
然后用了现在的方法:一行一对引号和一个换行符号
5、循环中continue没有存在的必要，去掉也行
'''

