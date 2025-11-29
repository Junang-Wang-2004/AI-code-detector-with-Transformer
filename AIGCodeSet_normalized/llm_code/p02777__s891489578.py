v1, v2 = map(list, input().split())
v3, v4 = map(int, input().split())
v5 = input()
if v5 == 'red':
    print(v3 - 1, v4)
elif v5 == 'blue':
    print(v3, v4 - 1)
else:
    print(v3, v4)
