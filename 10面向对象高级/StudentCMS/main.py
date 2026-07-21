"""
该文件 用作程序的入口文件
"""

from studentcms import StudentCMS

# 程序的主入口
if __name__ == '__main__':
    # 创建学生管理系统对象
    cms = StudentCMS()
    # 启动程序
    cms.start()