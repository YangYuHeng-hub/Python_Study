'''
格式化：
1.%d %s %f...
    print('%d %s %f' % (数字,字符串,浮点数))
2.format
'''
name = '赵丽颖'
age = 18

result = '美女{}今年{}岁'.format(name, age)
print(result)

# 使用数字填充，从0开始计数
result = '美女{0}今年{1}岁,我也是{1}岁'.format(name, age)
print(result)

# 使用变量名填充
result = '美女{name}今年{age}岁,我也是{age}岁'.format(name='赵丽颖', age='18')
print(result)

#
name = '小明'
score_chinese = 100
score_math = 99

s = '{0}本次考试的数学分数是：{1}，语文分数是：{2}，英语分数是：{1}'.format(name,score_math,score_chinese)
print(s)

s = '{name}本次考试的数学分数是：{score_math}，语文分数是：{score_chinese}，英语分数是：{score_english}'\
    .format(name='小明',score_math='99',score_chinese='100',score_english=score_math)
print(s)