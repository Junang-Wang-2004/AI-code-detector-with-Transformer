def f1():
    v1 = i_input()
    v2 = str(v1)
    for v3 in range(3):
        if v2[v3] == '1':
            print(9, end='')
        else:
            print(1, end='')
    print()
if __name__ == '__main__':
    f1()
