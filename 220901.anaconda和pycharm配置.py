''' 1.python项目和版本管理起来通常比较麻烦，不同的项目需要不同的python版本，可能造成混乱，
    所以需要anaconda来管理项目，Python版本和第三方库文件
    2.安装了anaconda之后，就不需要安装python了，如果想要安装其他版本，可以再在anaconda里面install
    例：conda create -n python3.9 python=3.9
    3.anaconda的安装和配置问题
     (1)可以在官网或者国内镜像网站下载anaconda安装包
     (2)下载好后打开安装包，使用选择all users，新版的anaconda的添加环境变量选项是无法勾选的，
        导致的结果是pycharm里可以找到conda里面的python，但是无法在cmd中直接敲python语句
     (3)安装好之后需要把conda的下载源添加国内镜像地址
        #查看当前conda配置
        conda config --show channels
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud//pytorch/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
        （清华源，暂时只找到这个，其他的有需要再找）
        #设置搜索是显示通道地址
        conda config --set show_channel_urls yes
     (4)手动添加环境变量，右键我的电脑->属性->高级系统设置->高级->环境变量->编辑系统环境变量里的path，添加5条
     *anaconda所在文件夹 C:\ProgramData\Anaconda3
     *anaconda里的Script C:\ProgramData\Anaconda3\Scripts
     *anaconda里的Library\bin C:\ProgramData\Anaconda3\Library\bin
     *anaconda里的Library\mingw-w64\bin C:\ProgramData\Anaconda3\Library\mingw-w64\bin
     **手敲Library\usr\bin C:\ProgramData\Anaconda3\Library\usr\bin
    4.PyChorm的安装和配置问题
     (1)到官网下载社会开源版(免费)，企业版免费使用一个月，官网如果打不开可以到国内镜像源里下载
     (2)下载好之后直接安装
'''