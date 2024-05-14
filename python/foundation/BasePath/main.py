# -- coding: utf-8 -
"""
@project    :HandBook
@file       :main.py
@Author     :wooght
@Date       :2024/5/14 19:51
@Content    :系统/路径
"""
import sys, os


"""
    sys 运行时的环境配置及资源
"""
print(sys.version.split(' '))       # python 版本信息
print(sys.argv[0])                  # 当前运行的python文件参数列表,0指当前文件名
# python mian.py abc    argv = ['main.py','abc']
print(sys.path)                     # 当前系统的环境变量, 可以导入包的路径
# ['E:\\wooght-server\\HandBook\\python\\foundation\\BasePath', 'E:\\wooght-server\\HandBook', 'D:\\Soft\\python312\\python312.zip', 'D:\\Soft\\python312\\DLLs', 'D:\\Soft\\python312\\Lib', 'D:\\Soft\\python312', 'D:\\Soft\\python312\\Lib\\site-packages']
sys.path.append(os.getcwd())        # 添加当前文件路径到环境变量
print(sys.path)
print(sys.executable)               # python 解释器路径
wait_input = input('请输入把内容:')
sys.stdout.write(wait_input)        # 标准输出 stdout.write() 不会换行
stdin = sys.stdin.readline()        # 等待标准输入
print(stdin)
print(sys.modules.keys())           # 返回已经导入的模块列表


"""
    os 操作系统相关命令
"""
path = os.path.abspath(__file__)    # 当前文件的绝对路径
print(path) # E:\wooght-server\HandBook\python\foundation\BasePath\main.py
print(os.path.basename(__file__))   # 当前文件名
pwd = os.getcwd()                   # 当前文件的绝对文件夹路径
print(pwd)  # E:\wooght-server\HandBook\python\foundation\BasePath
print(os.path.dirname(os.getcwd())) # 上一级目录,获取路径的目录
# E:\wooght-server\HandBook\python\foundation


def current_path():
    """current 当前"""
    print('main getcwd:{}'.format(os.getcwd()))

current_path()

"""
    os.path 不会英文调用而改变路径
"""
from abc_dir import abc
abc.now_pwd()

sys.exit()
