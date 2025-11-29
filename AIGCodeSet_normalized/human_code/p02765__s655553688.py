v1, v2 = map(int, input().split())
print(v2 if v1 >= 10 else v2 + 100 * (10 - v1))
