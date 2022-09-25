'''
空格处理：ljust,rjust,center,lstrip,rstrip,strip
strip: 去除左右侧空格
lstrip: 去除左侧空格
rstrip: 去除右侧空格
center(width): 把字符串放置于width长度的中央
ljust(width): 左对齐，总长度为width
rjust(width): 右对齐，总长度为width

字符串拼接：join
join: 将列表里的字符串元素拼接在一起
'''

# username = input('用户名:')
# print(len(username))
# result = username.strip()
# print(len(result))

words = ('you', 'and', 'me')
s = ''
result = s.join(words)
print(result)
