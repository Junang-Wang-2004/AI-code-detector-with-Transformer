v1 = input()
v2 = int(input())
for v3 in range(5 * 10 ** 15):
    v4 = ''
    for v5 in v1:
        if v5 == '1':
            v4 += '1'
        elif v5 == '2':
            v4 += '22'
        elif v5 == '3':
            v4 += '333'
        elif v5 == '4':
            v4 += '4444'
        elif v5 == '5':
            v4 += '55555'
        elif v5 == '6':
            v4 += '666666'
        elif v5 == '7':
            v4 += '7777777'
        elif v5 == '8':
            v4 += '88888888'
        elif v5 == '9':
            v4 += '999999999'
    v1 = v4
print(v1[v2 - 1])
