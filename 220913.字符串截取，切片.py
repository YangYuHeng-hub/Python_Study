'''
字符串
'''

s1 = 'hello'
s2 = s1
s3 = 'hello'
s4 = 'hello1'

print(s1, s2, s3)
# id(name),寻找name的内存地址
print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))

# is: A is B 如果AB地址相同，返回True，否则返回False
print(s1 is s2)
print(s1 is s4)

# 字符串截取
s1 = 'ABCDEFG'
'''
s1 A  B  C  D  E  F  G
   0  1  2  3  4  5  6
  -7 -6 -5 -4 -3 -2 -1
'''
# G G
print(s1[6], s1[-1])
print(len(s1))
'''
字符串索引机制：
1.0~len(s)-1
2.-len(s)~-1
'''

'''
切片：字符串，列表
格式：字符串变量[start:end]:取的到start，取不到end，[start,end)
     字符串变量[start:end:step]
'''
print(s1[1:4])
print(s1[-3:7])
print(s1[:5])  # 从0到下标为5的位置
print(s1[5:])  # 从5到结尾

print('*' * 20)

print(s1[:])
print(s1[::2])
# 取BDF
print(s1[1:-1:2])

'''
当step为负值时表示倒着取
取值逻辑：
num = s1[start]
if(num[start+step]<=end)
    print(num)
所以当step取负值时，相应的start和end也必须倒着取
'''
print(s1[7::-1])