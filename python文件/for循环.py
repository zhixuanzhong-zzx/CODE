'''
计数方式：用循环+变量加一
'''

count = 0
name = "zzx is one aaaaaof the best students in this world"
for x in name:
    if x == "a":
        count += 1

    print(f"{count}")
    
'''
这里运行后会发现前面有11个0，因为前11个字符都不是"a"，
可以看出for循环的遍历规则
要想显示字符串中a的个数为5，把最后一行顶格，移出循环外
'''
