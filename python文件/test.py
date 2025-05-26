time = 100
num = 1
x = f"钟志轩会坚持向死而生{100}年，会成功做好{"1*无数"}个产品"
print(x)

i = 3
if i == 3:
     print("zzzzz")

name = input("公司名字是？")
stock_price = 10.00
stock_code = "003032"
stock_price_daily_growth_factor = 1.1
growth_days = 8
y = stock_price*growth_days**stock_price_daily_growth_factor
print(f"""公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}
每日增长系数：{stock_price_daily_growth_factor}
经过{growth_days}的增长后，股价达到：{stock_price*growth_days**stock_price_daily_growth_factor}""")

a = 10 > 3
b = 10 < 3
print(f"{a and b}")
c = 1
d = 2
print(f"{c < d}")

