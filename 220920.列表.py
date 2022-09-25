'''
如何定义一个列表：
1.空列表：[]
2.初始化的列表：['A','B','C'],[1,2,3,4],[3.5,9.9,10]

里面可以存放的数据类型：
int
str
float
bool
list

列表操作：
获取里面的元素：list[index]
切片：list[start:end:step]  [start,end)
添加：
    append          list.append(value)      追加，在最后面加入
    extend          list1.extend(list2)     把list2加到list1中
                    list1=list1+list2       把list2加到list1中
    insert          list.insert(index,value)在index处插入value元素
删除：
    pop             list.pop(index)         删除list[index]
                    list.pop()              删除最后一个元素
    remove          list.remove(value)      删除第一个值为value的元素
    *关键字in        元素 in 列表              元素是否在列表中？返回值：bool
    clear           list.clear()            清空列表
    del             del list                删除list指针
修改：
                    list[index] = new       把index处的元素换成new
    *index          list.index(value)       找到list中第一个值为value元素的下标
查询：
    元素 in 列表
    列表.index(元素)
    count           list.count(value)       返回列表中元素的个数

排序：
    sort            list.sort()             默认升序
                    list.sort(reverse=True) 降序
'''

# list1 = ['牛奶', '辣条', '面包', '方便面', '火腿肠', '食盐', '臭豆腐']
# print(list1[::-3])
# print(list1[-2::-4])
# print(list1[::-1])
#
# list2 = [1, 2, 3]
# list1 = list1 + list2
# list1.extend(list2)
# print(list1)

'''
生成8个1-100之间的随机整数，保存到列表中
键盘输入一个1-100之间的整数，将整数插入到排序后的列表中(升降没有要求)
例：
[1,9,6,8,0]
[0,1,6,8,9]
5
[0,1,5,6,8,9]
'''

import random
list = []
for i in range(8):
    random_num = random.randint(0,100)
    list.append(random_num)
print(list)
list.sort()
print(list)
number = int(input('请输入一个1-100之间的整数:'))
if 0<=number<=100:
    for i in range(len(list)):
        if number<list[i]:
            list.insert(i,number)
            break
else:
    print('输入错误，请重新输入！')
print(list)
