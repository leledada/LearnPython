#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Car:
    def __init__(self, sp=50.0, pr=2.5):
        print('init a Car')
        self.speed = sp
        self.price = pr
        self.distance = 0

    def drive(self, distance):
        self.distance += distance
        print('distance', distance)
        print('total distance ', self.distance)
        print('time is ', distance / self.speed)
        print('cost is ', distance * self.price)


c1 = Car()
print("老司机1号")
c1.drive(500)
c1.drive(300)

print("老司机2号")
c2 = Car()
c2.price = 3
c2.speed = 100
c2.drive(1000)

print("老司机3号")
c3 = Car()
c3.price = 4
c3.drive(1000)

print("内置方法")
print(type(c1))
print(dir(c1))
print(isinstance(c1,Car))
print(isinstance(c1, dict))
print(c1.__dict__)
print(c1.__doc__)
