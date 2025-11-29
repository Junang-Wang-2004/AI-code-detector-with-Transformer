v1 = input()
v2 = [0] * 26
v3 = len(v1)
v4 = 1
for v5 in range(v3):
    v6 = ord(v1[v5]) - ord('a')
    v2[v6] += 1
for v5 in range(26):
    if v2[v5] == 0:
        print(chr(ord('a') + v5))
        v4 = 0
        break
if v4 == 1:
    print('None')
