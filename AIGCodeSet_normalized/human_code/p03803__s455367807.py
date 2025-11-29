v1 = [i for v2 in range(2, 15)]
v3, v4 = map(int, input().split())
print('Draw' if v4 == v3 else 'Alice' if v1[v3 - 2] > v1[v4 - 2] else 'Bob')
