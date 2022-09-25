# 字符串如何进行格式化？
'''
符号：
%s 字符串 string
%d 整数 digit
%f 浮点数 float

'''

name = '杨育恒'
age = 23
print('我叫%s，我今年%d岁' % (name,age))

money = 12.50
# 我叫杨育恒，我今年23岁，花12.500000块钱买了一支笔
print('我叫%s，我今年%d岁，花%f块钱买了一支笔' % (name,age,money))

# 我叫杨育恒，我今年23岁，花12.5块钱买了一支笔
print('我叫%s，我今年%s岁，花%s块钱买了一支笔' % (name,age,money))# str(age) str(money)

# 我叫杨育恒，我今年23岁，花12.50块钱买了一支笔  %.2f保留2位小数
print('我叫%s，我今年%d岁，花%.2f块钱买了一支笔' % (name,age,money))