v1 = input()
v2 = int(input())
v3 = [v1[i] for v4 in range(len(v1)) if v4 % v2 == 0]
print(''.join(v3))
