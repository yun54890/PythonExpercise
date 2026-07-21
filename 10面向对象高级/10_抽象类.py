"""
抽象类（接口）
"""


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪叫")

class Cat(Animal):
    def speak(self):
        print("喵喵叫")



if __name__=="__main__":
    dog = Dog()
    dog.speak()
    cat = Cat()
    cat.speak()