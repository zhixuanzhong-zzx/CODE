def make_counter():
    count = 0        # 外层作用域的变量
    def counter():   # 内层函数（闭包）
        return count
    return counter   # 返回闭包函数

# 调用外层函数，返回闭包函数
counter1 = make_counter()  # 第一次调用，创建 count=0
print(counter1())  # 0（返回闭包变量 count）
print(counter1())  # 0（继续返回同一个 count）

counter2 = make_counter()  # 第二次调用，创建新的 count=0（独立作用域）
print(counter2())  # 0（新的闭包，新的 count）
