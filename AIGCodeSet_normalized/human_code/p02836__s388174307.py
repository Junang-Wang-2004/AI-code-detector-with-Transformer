v1 = input()
v2 = v1[0:len(v1) // 2]
v3 = v1[len(v2):len(v1)]
v3 = v3[::-1]
v4 = 0
for v5, v6 in zip(v2, v3):
    if v5 != v6:
        v4 += 1
print(v4)
