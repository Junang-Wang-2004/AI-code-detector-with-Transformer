v1, v2 = map(int, input().split())
print('Draw' if v1 == v2 else 'Alice' if v1 > v2 or v2 == 1 else 'Bob')
