'''
字典
dict{key1:value1 , key2:value2}
字典的键是无法修改的，只能修改对应的值
dict[key1] = 修改的_value1

键可以添加和删除,键是唯一的，如果字典中存在键，则是修改，如果不存在，则是添加
dict[new_key] = new_value

'''

dict1 = {'name':'张三','age':'18','sex':'男'}
print(dict1['name'])


'''
练习:
book = {}
书名，价格，作者，出版社
促销：价格折扣 8折
打印最终字典中的内容
'''

book = {
    '书名':'《三体》',
    '价格':18,
    '作者':'刘慈欣',
    '出版社':'**出版社'
}
#修改价格
book['价格'] *= 0.8 # book['价格'] = book['价格']*0.8
print(book)

'''
字典删除：

dict.clear()           清空
dict.pop(key)          删除指定键值对
dict.popitem()         删除最后一对键值对
del dict               删除字典结构

'''

'''
根据key得到value值:

如果key不存在，则会报错
value = dict[key]

如果key不存在，则value=None
value = dict.get(key)
而且get还可以设置默认值,key不存在，则value=默认值
value = dict.get(key,默认值)
'''

'''
字典遍历

如果使用for..in直接遍历字典，取出来的是key
for i in dict:
    print(i)   # key1 key2...
要先使用dict.values()
dict.values() ===> dict_values([value1,value2,...])
for i in dict.values():
    print(i)   # value1
                 value2
                 ...

相应的字典也有dict.keys()
dict.keys() ===> dict_keys([key1,key2,...])

dict.items()
dict.items() ===> dict_items([(key1, value1), (key2, value2), ...])
for i in book.items()
    print(i) # (key1,value1)
               (key2,value2)
               ...
for k,v in book.items()
    print(k,v) # key1 value1
                 key2 value2
                 ...
'''
print(book.items())

'''
dict.setdefault(key,value)
只能添加，不能修改
'''

'''
dict.update(add_dict)
将add_dict加入到dict中
'''

'''
dict1 = dict.fromkeys([key1,key2],value)
初始化一个字典
print(dict1) # {key1:value , key2:value}
'''