v1 = int(input())
v2 = v1 + 1
while True:
    if len(set(str(v2))) == 1:
        print(v2)
        break
    v2 += 1
