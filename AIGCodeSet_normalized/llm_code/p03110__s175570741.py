v1 = int(input())
v2 = 0
for v3 in range(v1):
    v4, v5 = input().split()
    if v5 == 'JPY':
        v2 += int(v4)
    else:
        v2 += 380000.0 * float(v4)
print(v2)
