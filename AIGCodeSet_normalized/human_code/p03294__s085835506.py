def f1():
    *v1, = map(int, open(0).read().split())
    print(sum(v1[1:]) - v1[0])
if __name__ == '__main__':
    f1()
