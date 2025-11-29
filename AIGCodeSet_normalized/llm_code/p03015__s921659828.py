v1 = input()
v2 = 10 ** 9 + 7

def f1(a1):
    if a1 == '0' or a1 == '':
        return 1
    if a1 == '1':
        return 3
    if a1[0] == '0':
        return f1(a1[1:])
    else:
        v1 = a1[1:]
        return (pow(2, len(v1), v2) + f1(v1)) % v2
print(f1(v1))
