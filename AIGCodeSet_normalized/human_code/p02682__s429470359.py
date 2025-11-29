def f1():
    v1, v2, v3, v4 = map(int, input().split())
    if v4 <= v1 + v2:
        print(min([v1, v4]))
    else:
        print(v1 - (v4 - v1 - v2))
if __name__ == '__main__':
    f1()
