#!/usr/bin/python3
# -*- coding: utf-8 -*-


def my_input(msg):
    my_num = input(msg)
    while not my_num.isdigit():
        print("输入有误，请重新输入整数")
        my_num = input(msg)
    return my_num


m = my_input("heads(m):")
n = my_input("feets(n):")


def count_cock(m, n):
    for cock in range(m):
        rabbit = m - cock
        if n == rabbit * 4 + cock * 2:
            print("cocks: ", cock, "rabbits: ", rabbit)
            return
    print("invalid input")


if __name__ == "__main__":
    count_cock(int(m), int(n))
