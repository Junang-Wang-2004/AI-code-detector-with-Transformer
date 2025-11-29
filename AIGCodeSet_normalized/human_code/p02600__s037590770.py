def f1():
    v1 = int(input())
    v2 = 400
    v3 = 599
    v4 = 8
    for v5 in range(8):
        if v2 <= v1 <= v3:
            print(v4)
            return
        v2 += 200
        v3 += 200
        v4 -= 1
if __name__ == '__main__':
    f1()
