def f1():
    v1 = input()
    v2 = ''.join(list(reversed(v1)))
    if v1 == v2:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    f1()
