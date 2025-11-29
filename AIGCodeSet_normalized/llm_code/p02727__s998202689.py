def f1():
    return map(int, input().split())

def f2():
    return list(map(int, input().split()))
v1, v2, v3, v4, v5 = f1()
v6 = f2()
v7 = f2()
v8 = f2()
v6.sort(reverse=True)
v7.sort(reverse=True)
v8.sort(reverse=True)
v6 = v6[:v1]
v7 = v7[:v2]
v8 = v8[:v1 + v2 - len(v6) - len(v7)]
v9 = v6 + v7 + v8
v9.sort(reverse=True)
v10 = sum(v9[:v1 + v2])
print(v10)
