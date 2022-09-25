'''
运算符
算术运算符 + - * / % //(整除) **(幂运算)
'''

# a = 1
# b = 2
# c = a + b
# # sep分隔符默认为' ',end结尾默认为'\n'
# print(a, b, c, sep='#', end='')
#
# # 1.5 1 9
# print(c / 2, c // 2, c ** 2)

'''
键盘输入一个三位数整数，打印个位数，十位数，百位数
'''
# num = int(input('请输入一个三位数：'))
# print(num % 10)
# print(num // 10 % 10)
# print(num // 100)

'''
赋值运算符
=
+=
-=
*=
/=
//=
**=
%=
'''

# a = 3
# b = 5
# c = a + 1
# print(a, b, c)
# a += 1 #a = a + 1
# b -= 1 #b = b - 1
# c *= 2 #c = c * 2
# print(a,b,c)
#
# a /= 2 #a = a / 2
# b //= 3 #b = b // 3
# c **= 2 #c = c**2
# print(a,b,c)
#
# c %= a
# print(c)

'''
关系运算符： 结果：True False
>  <  >=  <=  ==  != is
'''
# a = 10
# b = 34
# print(a > b)
# print(a < b)

# 字符串比较机制，逐个对比，当遇到第一个不同的字母时，比较两者ASCII码
# x = 'abc'
# y = 'abbd'
# print(x<y)

'''
逻辑运算符：
and or not is
逻辑运算符的优先级低于关系运算符
'''
a = 1
b = 2
print(a and b)  # and 两边都是非0数字，结果为后面那个
c = 0
print(c and a)  # and 两边只要有一个为0，结果为0
print('#' * 20)  # 打印20个#号
