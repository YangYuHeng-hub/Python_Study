'''
王者荣耀角色管理

角色： 姓名，性别，职业
添加角色
删除角色
修改角色
查询角色 单个角色
显示所有角色
退出系统

'''
import time

all_role = [
    ['赵云','男','刺客'],
    ['貂蝉','女','法师']
            ] #存放所有角色的容器
print('**********欢迎进入王者荣耀角色管理**********')
while True:
    choice = input('请选择功能：\n 1.添加角色\n 2.删除角色\n 3.修改角色\n 4.查询角色\n 5.显示所有角色\n 6.退出系统\n')
    #判断
    if choice == '1':
        print('添加角色模块：')
        name = input('\t角色名：')
        sex = input('\t性别：')
        major = input('\t职业：')
        role = [name,sex,major]
        all_role.append(role)
        print('成功添加{}到王者荣耀系统!\n'.format(name))

    elif choice == '2':
        print('删除角色模块：')
        role_name = input('输入要删除的角色名：')
        for role in all_role:
            if role_name in role:
                #? 添加一个是否删除的询问
                isDelete = input('是否删除{}?(y/n)'.format(role_name))
                if isDelete == 'y' or isDelete == 'Y':
                    all_role.remove(role)
                    print('成功删除{}'.format(role_name))
                    break
        else:
            print('不存在角色：{}，请检查角色名'.format(role_name))

    elif choice == '3':
        print('修改角色模块：')
        role_name = input('输入要修改的角色名：')
        for role in all_role:
            if role_name in role:
                print('{}{}{}'.format('名称'.center(10),'性别'.center(10), '职业'.center(10), ))
                print(role[0].center(10), end='')
                print(role[1].center(10), end='')
                print(role[2].center(10))
                while True:
                    edit_part = input('请输入要修改的内容：(1.角色名 2.性别 3.职业)')
                    if edit_part == '1':
                        role[0] = input('角色名：')
                    elif edit_part == '2':
                        role[1] = input('性别：')
                    elif edit_part == '3':
                        role[2] = input('职业：')
                    else:
                        print('选择错误，请重新输入')
                        continue
                    print('修改成功！')
                    print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10), ))
                    print(role[0].center(10), end='')
                    print(role[1].center(10), end='')
                    print(role[2].center(10))
                    break
                break
        else:
            print('不存在角色：{}，请检查角色名'.format(role_name))

    elif choice == '4':
        print('查询角色模块：')
        role_name = input('输入要查询的角色名：')
        for role in all_role:
            if role_name in role:
                print('{}{}'.format('性别'.center(10), '职业'.center(10), ))
                print(role[1].center(10), end='')
                print(role[2].center(10))
                break
        else:
            print('不存在角色：{}，请检查角色名'.format(role_name))

    elif choice == '5':
        print('显示所有角色模块：')
        print('{}{}{}'.format('名称'.center(10),'性别'.center(10),'职业'.center(10),))
        for role in all_role:
            print(role[0].center(10),end='')
            print(role[1].center(10),end='')
            print(role[2].center(10))

    elif choice == '6':
        print('正在退出王者荣耀管理系统...')
        time.sleep(1)
        print('成功退出')
        break

    else:
        print('输入错误，请重新选择!')