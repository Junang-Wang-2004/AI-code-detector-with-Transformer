v1 = list(map(int, input().split()))
print(v1)
print(v1[1])
if sorted(v1) == [5, 5, 7]:
    print('YES')
else:
    print('NO')
