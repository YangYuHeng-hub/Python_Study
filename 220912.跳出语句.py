'''
break跳出循环结构
continue跳过本次循环，后面的语句不执行了
'''

# 不打印能被3整除的

# for i in range(10):
#     if i % 3 != 0:
#         print(i)

for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
