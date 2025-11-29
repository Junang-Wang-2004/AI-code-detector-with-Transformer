def f1():
    v1, v2, v3 = [int(i) for v4 in input().split()]
    if abs(v1 - v2) < abs(v1 - v3):
        print('A')
    else:
        print('B')
if __name__ == '__main__':
    f1()
