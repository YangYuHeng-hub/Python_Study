'''
1.键盘上输入以下内容并打印输出：
默认（admin，1234）
用户名：username
密码：password
是否记住密码bool类型，is_remember

如果用户名和密码正确并且 is_remember 是True表示记住密码，则打印已经记住用户xxx
的密码啦
否则打印，没有记住密码需要下次继续输入
'''

username = 'admin'
password = '1234'
is_remember = False

nameInput = input('请输入用户名：')
passwordInput = input('请输入密码：')

if nameInput == username and passwordInput==password:
    if is_remember:
        print('已经记住用户%s的密码啦' % username)
    else:
        print('没有记住密码需要下次继续输入')
else:
    print('用户名或密码有误！')
