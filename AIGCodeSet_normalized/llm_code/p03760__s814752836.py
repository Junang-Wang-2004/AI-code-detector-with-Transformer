v1 = input()
v2 = input()
v3 = ''
for v4, v5 in zip(v1, v2):
    v3 += v4 + v5
print(v3 + v1[-1] if len(v1) > len(v2) else v3)
