import sys
v1 = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
v2 = sys.stdin.buffer.readlines

def f1():
    v1 = int(input())
    v2 = 0
    if v1 >= 105:
        v2 += 1
    if v1 >= 135:
        v2 += 1
    if v1 >= 165:
        v2 += 1
    if v1 >= 189:
        v2 += 1
    if v1 >= 195:
        v2 += 1
    print(v2)
if __name__ == '__main__':
    f1()
