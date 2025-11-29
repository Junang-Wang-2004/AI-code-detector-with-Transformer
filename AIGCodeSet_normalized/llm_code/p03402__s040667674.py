v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1
v3, v4, v5, v6 = (v1 // 10, v1 % 10, v2 // 10, v2 % 10)
for v7 in range(100):
    if v7 % 2 == 0:
        if v7 // 2 + 1 <= v3:
            v8 = '.#' * 10 + '.' * 79 + '#'
            print(v8)
        elif v7 // 2 + 1 == v3 + 1:
            v8 = '.#' * v4 + '.' * (100 - 2 * v4 - 1) + '#'
            print(v8)
        else:
            print('.' * 99 + '#')
    elif v7 // 2 + 1 <= v5:
        v8 = '.' + '#' * 79 + '.#' * 10
        print(v8)
    elif v7 // 2 + 1 == v5 + 1:
        v8 = '.' + '#' * (100 - 2 * v6 - 1) + '.#' * v6
        print(v8)
    else:
        print('.' + '#' * 99)
