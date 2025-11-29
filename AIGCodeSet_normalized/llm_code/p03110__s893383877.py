v1 = 0
v2 = int(input())
for v3 in range(v2):
    v4 = input().split(' ')
    v1 += float(v4[0]) if v4[1] == 'JPY' else float(v4[0]) * 380000.0
print(v1)
