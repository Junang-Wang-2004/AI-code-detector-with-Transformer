v1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
v2 = str(input())
v3 = None
for v4 in range(26):
    if v1[v4] not in v2:
        v3 = v1[v4]
        break
print(v3)
