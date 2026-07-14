"""
import 和 from 语句中
是用来区分层级的
"""

# import my_package.module1
# import my_package.module2
#
#
# my_package.module1.hi()
# my_package.module2.haha()

# import my_package.module1 as m1
# import my_package.module2 as m2
# m1.hi()
# m2.haha()


# from my_package import module1 as m1
# m1.hi()
# from my_package.module1 import hi
# hi()


from my_package import *
module1.hi()
