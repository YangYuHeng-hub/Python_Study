'''
循环：
场景：
1.用户名和密码，反复输入
2.计算1-100
3.游戏死亡重生

方式：
1.while
2.for

while格式：
while 条件（布尔类型）：
    要循环执行的代码
'''

# n = 1
# sum = 0
# while n <= 10:
#     sum = sum + n
#     n += 1
# print(count)

'''
猜数：
1.产生随机数
2.可以猜多次，直到猜对为止，如果猜错，给出猜大了或猜小了
3. 1次猜中，运气爆棚
   2-5次猜中，运气不错
   6次猜中，运气有点差 
'''
# import random
#
# random_num = random.randint(1, 10)
# count = 0
# while True:
#     count += 1
#     num = int(input('请输入1-10中您猜的值：'))
#     if num == random_num:
#         print('恭喜您猜对了')
#         break
#     elif num > random_num:
#         print('猜大了，请重新再猜')
#     else:
#         print('猜小了，请重新再猜')
# if count == 1:
#     print('运气爆棚了')
# elif 2 <= count <= 5:
#     print('运气不错哟')
# else:
#     print('运气有点差')


'''
for循环
格式：
for i in range(n):
    循环体中的内容
    
for i in range(n):
    循环体
else:
    如果for循环0-n-1没有出现中断
    
相同的，也有while...else
    
range(n):从0开始取值到n-1结束
range(start,stop):[start,stop)
range(start,stop,step):start+k(step),k=0,1,2,3....
'''

# for i in range(10):
#     print(i)

# 最多输入用户名和密码三次，如果3次没有登陆成功，提示账号被锁定
for i in range(3):
    username = input("用户名：")
    password = input("密码：")
    if username == 'admin' and password == '123':
        print("登陆成功！")
        break
    print("用户名或密码有误\n")
    # if i == 2:
else:
    print("账户被冻结！")

n = 1
while n <= 10:
    print(n)
    n += 1
    if n == 5:
        break
else:
    print('over')
