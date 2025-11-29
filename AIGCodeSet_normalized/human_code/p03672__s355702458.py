def f1(a1):
    if len(a1) % 2 == 1:
        return False
    elif a1[:len(a1) // 2] == a1[len(a1) // 2:]:
        return True
    else:
        return False
v1 = input()
for v2 in range(len(v1) - 1, 0, -1):
    if f1(v1[:v2]):
        print(len(v1[:v2]))
        break
