v1 = int(input())
for v2 in range(1, 50001):
    if int(v2 * 1.08) == v1:
        print(v2)
        exit()
print(':(')
