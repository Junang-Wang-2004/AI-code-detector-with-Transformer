import sys
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
v4, v5, v6, v7, v8 = v3()
v9 = v3()
v9.sort(reverse=True)
v10 = v3()
v10.sort(reverse=True)
v11 = v3()
v11.sort(reverse=True)
v9 = v9[:v4]
v10 = v10[:v5]
v12 = v9 + v10 + v11
v12.sort(reverse=True)
v13 = sum(v12[:v4 + v5])
print(v13)
