'''
替换内容：replace
replace(old,new,count): 从左至右的count个old全部换成new，count不填的话默认为全部

切割字符串：split，rsplit，splitlines，partition，rpartition
split('分隔符',num): 从左往右切num次，返回的结果是一个列表
rsplit('分割符',num): 从右往左切割num次，返回的结果是一个列表
splitlines: 按行分割
partition('分隔符'): 用给定分隔符把目标分成(分隔符前面部分,分隔符,分隔符后面部分)
rpartition('分隔符'): 同partition,从右往左寻找分隔符

修改大小写：capitalize，title，upper，lower
capitalize: 把第一个字母变成大写
title: 每个单词的首字母变成大写
upper: 每个字母都变成大写
lower: 每个字母都变成小写
'''

# s = 'what are you doing? who are you?'
# result = s.replace('you', '**', 1)
# 替换you和are  1.正则表达式  2.for循环+列表
# result = s.replace()
# print(result)

# s = 'you me he'
# result = s.split(' ')
# print(result)

# s = '''what
# are
# you
# doing
# ?
# '''
# result = s.splitlines()
# print(result)

# s = 'you and me'
# result = s.partition(' ')
# print(result)

s = 'hello world'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())