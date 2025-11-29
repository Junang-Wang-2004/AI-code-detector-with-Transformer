v1 = int(input())
v2 = int(v1 // 1.08)
while int(v2 * 1.08) != v1:
    v2 += 1
    if v2 * 1.08 > v1:
        print(':(')
        exit()
print(v2)
