path = 'file:///C:/Users/Huan/Documents/WeChat%20Files/wxid_8wj6zv72irkg22/FileStorage/File/2022-09/2022%E7%BA%A7%E7%8F%AD%E7%BA%A7%E5%88%86%E6%B5%81%E6%8C%87%E5%8D%97.pdf'

'''
查找
find,index,rfind,rindex
find:从左向右查找，只要遇到一个符合要求的则返回位置，如果没有找到任何符合要求的则返回-1
rfind:从右往左查找
count:统计指定字符的个数
index和find的区别：index也是表示查找，但是如果找不到会报错
'''
# i = path.rfind('/')
# print(path[i+1:])
#
# print(path.count('/'))


'''
判断
startswith,endswith,isalpha,isdigit,isalnum,isspace
isupper,islower
返回值都是布尔类型的（True，False）
startswith(关键词): 是否以关键词开头的
endswith(关键词): 是否以关键词结尾的
isalpha: 是否全部是字母
isdigit: 是否全部是数字
isalnum: 是否是字母或者数字
isspace: 是否全部是空格
isupper: 是否全部是大写字母
islower: 是否全部是小写字母
'''

'''
模拟文件上传，键盘输入上传文件的名称，判断文件名是否大于6位，扩展名是否是：jpg，png，gif格式
如果不是则提示上传失败，如果名字不满足要求，而扩展名满足条件则随机生成一个6位数字组成的文件名，打印成功上传xxxxxx.png
'''
# import random
#
# file = input('请输入您要上传的文件：')
# dot_index = file.rfind('.')
# expandedName = file[dot_index + 1:]
# file_name = file[:dot_index]
# if expandedName == 'jpg' or expandedName == 'png' or expandedName == 'gif':
#     if len(file_name) >= 6:
#         print('成功上传%s' % file)
#     else:
#         random_name = ''
#         for i in range(6):
#             random_name += str(random.randint(0, 9))
#         print('成功上传%s.%s' % (random_name,expandedName))
# else:
#     print('上传失败')

'''
用户名或者手机号码登录+密码
用户名：全部小写，首字母不能是数字，长度必须6位以上
手机号码：纯数字 长度11
密码必须是6位数字
以上格式符合要求则进入验证

admin123
15811119999
200325

判断是否验证通过
'''

# username = input('请输入用户名或手机号：')
# if username.islower() and ~(username[0].isdigit()) and len(username)>=6:
#     if username != 'admin123':
#         print('输入错误')
#         exit()
# elif username.isdigit() and len(username)==11:
#     if username != '15811119999':
#         print('输入错误')
#         exit()
# else:
#     print('输入错误')
#     exit()
#
# password = input('请输入密码：')
# if password.isdigit() and len(password)==6:
#     if password == '200325':
#         print('登陆成功')
#     else:
#         print('密码错误，登陆失败')
# else:
#     print('密码格式不正确，登陆失败')



