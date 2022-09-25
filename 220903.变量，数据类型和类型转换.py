'''
变量：’容器‘
弱语言： 变量声明的时候对数据类型不严格
Java： int a = 100
python： a = 100

格式： 变量名=值
1.怎么起名
2.可以赋什么值
3.有哪些数据类型

变量名的命名规范：
1.字母，数字，下划线，其他特殊符号不行
2.不能数字开头
3.不能使用关键字
4.严格区分大小写
见名知义：getnamebyid
getNameById 驼峰式： 开头第一个单词全部小写，小驼峰
每一个单词首字母都大写，面向对象，类名，大驼峰
get_name_by-id python更建议用下划线

数据类型：
1.Number
    int
    long
    float
    complex(复数)
2.布尔类型
    True
    False
3.String
4.List
5.Tuple(元组)
6.Dictionary(字典)
'''

money = 28
# <class 'int'>
print(type(money))

money = 28.9
# <class 'float'>
print(type(money))

money = 8.4234324
# <class 'float'>
print(type(money))

money = '一万'
# <class 'str'>
print(type(money))

money = '''10000'''
# <class 'str'>
print(type(money))

message = '我说："hello"'
# 我说："hello"
print(message)
message = "我说：'hello'"
# 我说：'hello'
print(message)

poem = '''
        静夜思
        作者：李白
    床前明月光，疑是地上霜。
    举头望明月，低头思故乡。
'''
# 三引号是保留格式的字符串
print(poem)

# 布尔类型：True False
isLogin = True #真
print(isLogin)
isLogin = False #假
print(isLogin)

#类型转换
#str---->int
money = input('请输入金额')
#input传进来的都是字符串类型,要先转换成int类型才能计算
print(int(money)+1000)
#int---->str
print(money+str(1000))