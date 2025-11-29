def f1(a1):
    if a1 % 2 != 0:
        return 'No'
    else:
        v1 = a1 // 2
        v2 = []
        for v3 in range(v1):
            v2.append([v3 * 2 + 1, v3 * 2 + 2])
        return 'Yes\n' + str(v1) + '\n' + '\n'.join(['2 ' + ' '.join((str(x) for v4 in s)) for v5 in v2])
v1 = int(input())
print(f1(v1))
