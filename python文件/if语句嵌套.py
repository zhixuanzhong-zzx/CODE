if int(input("你的身高：")) > 120:
    print("""没满足身高要求
    可以看看vip等级合适吗""")
    if int(input("vip等级是：")) >= 3:
        print("满足了，免费来")
    else:
        print("买票吧，兄der")
else:
    print("身高满足了，免费来")

age = int(input("你的年龄："))

if age > 18:
    if age < 30:
        if int(input("入职时间：")) > 2:
            print("入职时间满足，免费")
        elif int(input("等级：")) > 3:
            print("等级满足，免费")
        else:
            print("年龄ok，其他两项不ok")
    else:
        print("年龄太大，不ok")
else:
    print("小屁孩，gun")