#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Vehicle:
    def __init__(self, sp=50.0):
        print('init a Vehicle')
        self.speed = sp
        self.distance = 0

    def drive(self, distance):
        self.distance += distance
        print('distance', distance)
        print('total distance ', self.distance)
        print('time is ', distance / self.speed)


class Bike(Vehicle):
    def __init__(self, sp=20.0):
        super(Bike, self).__init__(sp)
        print('init a Bike _o-|-o_')


class Bus(Vehicle):
    def __init__(self, sp=60.0, pr=2.5):
        super(Bus, self).__init__(sp)
        self.price = pr
        print('init a Bus __----__')

    def drive(self, distance):
        self.distance += distance
        print('distance', distance)
        print('total distance ', self.distance)
        print('time is ', distance / self.speed)
        print('cost is ', distance * self.price)


print('父类开车')
v1 = Vehicle()
v1.drive(100)

print('\n子类BUS开车')
b1 = Bus()
b1.drive(100)

print('\n子类Bike开车')
b2 = Bike()
b2.drive(100)
