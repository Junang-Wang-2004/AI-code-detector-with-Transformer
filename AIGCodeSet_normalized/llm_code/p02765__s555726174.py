def f1():
    v1, v2 = map(int, input().split())
    if v1 >= 10:
        return v2
    else:
        return v2 + 100 * (10 - v1)
if __name__ == '__main__':
    print(f1())
