v1, v2 = map(int, input().split())
v3 = []
for v4 in range(40):
    if v1 >= v2 ** v4:
        v3.append(v4)
    else:
        break
print(v3[-1] + 1)
