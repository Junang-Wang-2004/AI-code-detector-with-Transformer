v1, v2 = input().split()
v1, v2 = (int(v1), int(v2))
print('Alice' if v1 > v2 else 'Bob' if v2 > v1 else 'Draw')
