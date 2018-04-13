class Human():
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 1000:
            raise ValueError('人不可能活这么久的')
        self.__age = age


s1 = Human('leledada')
print(type(s1))
s1.age = 10
print(s1.age)
s1.age = 10000
