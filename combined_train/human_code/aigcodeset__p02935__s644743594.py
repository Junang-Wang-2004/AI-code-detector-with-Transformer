def f1(a1):
    v1 = 0
    v1 += (a1[0] + a1[1]) / 2
    v2 = len(a1)
    v3 = 2
    while v2 > 2:
        v1 += a1[v3]
        v1 /= 2
        v2 -= 1
        v3 += 1
    return v1
v1 = int(input())
v2 = 0
v3 = list(map(int, input().split()))
v3.sort()
'\nif n>2:\n    for i in range(2,n):\n        ans=(v[0]+v[1])*(2**(-n+1))+v[i]*(2**(-n+i))\nelse:\n    ans=(v[0]+v[1])*(2**(-n+1))\n'
v2 = f1(v3)
if v2 - int(v2) == 0:
    print(int(v2))
else:
    print(v2)
