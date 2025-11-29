"""
Created on 2019/3/
Solved on 2019/3/
@author: shinjisu
"""

def f1():
    return int(input())

def f2():
    return [int(x) for v1 in input().split()]

def f3(a1):
    return [0] * a1

def f4(a1):
    return [int(input()) for v1 in range(a1)]
'\ndef getIntLines(n):\n    data = zeros(n)\n    for i in range(n):\n        data[i] = getInt()\n    return data\n'

def f5(a1, a2):
    return [f3(a2)] * a1

def f6(a1, a2):
    v1 = f5(a1, a2)
    for v2 in range(a1):
        v1[v2] = f2()
    return v1
v1 = [chr(i + ord('a')) for v2 in range(26)]
v3 = [chr(v2 + ord('0')) for v2 in range(10)]
v4 = 10 ** 9 + 7
v5 = 10 ** 18

class C1:

    def __init__(self):
        self.debug = True

    def off(self):
        self.debug = False

    def dmp(self, a1, a2=''):
        if self.debug:
            if a2 != '':
                print(a2, ':  ', end='')
            print(a1)
        return a1

def f9(a1, a2):
    global K
    if a2 >= a1[-1]:
        return -1
    else:
        for v1 in range(K):
            if a2 == a1[v1]:
                return 0
            elif a2 < a1[v1]:
                a1[v1 + 1:] = a1[v1:-1]
                a1[v1] = a2
                break
    return 0

def f10():
    global K
    v1 = C1()
    v1.off()
    v2 = input()
    v1.dmp(v2)
    v3 = f1()
    v1.dmp(v3)
    v4 = ['~' for v2 in range(v3)]
    for v5 in range(len(v2)):
        for v6 in range(v5, len(v2)):
            if f9(v4, v2[v5:v6 + 1]):
                break
    return v4[-1]
v6 = f10()
if v6 is None:
    pass
elif type(v6) == tuple and v6[0] == 1:
    for v7 in v6[1]:
        print(v7)
else:
    print(v6)
