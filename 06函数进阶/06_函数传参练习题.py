
def func(name,age,*args,**kwargs):
        print(f"我是{name}，年龄{age}岁，我的爱好有：",end="")
        for i in args:
            print(f"{i}",end=" ")
        print()
        print(f"我的其他信息：")

        for key in kwargs:
            print(f"{key}:{kwargs[key]}",end="、")


func("周杰伦","20","唱","跳","rap",gengder="男",address="深圳")