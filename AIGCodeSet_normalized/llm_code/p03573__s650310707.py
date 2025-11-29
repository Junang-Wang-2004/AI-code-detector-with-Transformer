v1, v2, v3 = map(int, input().split())
print(v1 if v2 == v3 else v2 if v1 == v3 else v3)
