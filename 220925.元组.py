'''
Python的元组与列表类似，不同之处在于元组的元素不能修改（增删改）.
元组使用小括号()，列表使用方括号[]

list 列表
tuple 元组

定义：
    名 = ()
    注意：如果元组中只有一个元素，必须添加逗号 ('aaa',) (1,) (2.8,)
下标+切片
方法：
    count()
    index()
关键字：
    in, not in
    for...in
    while
转换：
    list(tuple) ---->元组转列表
    tuple(list) ---->列表转元组
'''

t1 = ()
print(type(t1))

t2 = ('aa',)  # <class 'str>--('aa')  |  <class 'tuple'>--('aa',)
print(type(t2))

t3 = ('a', 'b', 'c')
print(type(t3))

# 下标和切片   字符串，列表，元组 一定要注意下标越界问题
print(t3[1])
print(t3[1:])
print(t3[::-1])

# 计数
print(t3.count('a'))

# tuple.index(元素，start,end),从start到end [start,end) ,找返回第一个元素值的下标
# 注意：当index没有找到元素时，会报错
print(t3.index('a', 1))

'''
支持：
len
in,not in
for...in
'''
