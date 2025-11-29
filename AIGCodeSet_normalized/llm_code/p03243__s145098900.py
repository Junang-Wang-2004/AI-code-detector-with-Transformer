v1 = int(input())
for v2 in range(v1, 10000):
    if len(set(str(v2))) == 1:
        print(v2)
        break
