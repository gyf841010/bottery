#!/usr/bin/python
# coding=utf-8

def gen_lottery():
    lottery = []
    from random import randint

    while len(lottery) < 6:
        x = randint(1, 49)
        if x in lottery:
            continue
        lottery.append(x)
    lottery.sort()
    return lottery


if __name__ == '__main__':
    lottery = gen_lottery()
    print("Results: ", lottery)