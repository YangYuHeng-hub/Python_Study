#   单行注释
''' 多行注释 '''

# 快捷键：
'''
ctrl+/ 单行注释
ctrl+alt+l 代码格式化
ctrl+y 删除一行
ctrl+d 复制一行
'''

# 第三方库管理
'''
File->Setting->Project->Python Interpreter
注： 1.虽然pycharm也能搜索和下载包，但是总是会遇到有些包下载失败或者查询不到的情况
    因此一般用anaconda来管理包
    2.当我们需要用到其他版本的python时，只需要在anaconda中建立一个新环境：
    conda create -n python36 python=3.6（例，安装一个3.6版本的python）
    然后在pycharm里的Python Interpreter中添加已安装好的3.6版本
    3.anaconda安装包的方法
    首先cmd定位到anaconda的script文件夹，然后pip install 包名
    安装完成后，可以在pycharm中看到
'''
