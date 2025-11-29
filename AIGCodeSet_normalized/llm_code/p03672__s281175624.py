v1 = input()
while len(v1) % 2 != 0 or v1[:len(v1) // 2] != v1[len(v1) // 2:]:
    v1 = v1[:-1]
print(len(v1))
