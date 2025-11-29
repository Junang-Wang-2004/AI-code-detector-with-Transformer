"""
xi,xjのペアにおいて、このペアは何通り出てくるか
sum(全通り)sum(i)sum(j){|xi-xj|+|yi-yj|}
和なので、どんな順序でもいい

sum(i)sum(j)sum(全通り){|xi-xj|}
sum(i)sum(j)sum(全通り){|yi-yj|}

あるi,jで固定して、sum(全通り){|xi-xj|}を求めるヤツ
固定したi,jが現れる回数は、

pat = NM-2_C_K-2 こいつはどこでも一緒

pat*sum(i)sum(j){|xi-xj|}を計算する
すべてのi,j(i>j)ペアにおいて、xi,xjの和は
sum(i=1,N){i*(N-i)}
"""
from math import factorial
v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = 1
v6 = v1 * v2 - 2

def f1(a1, a2, a3):
    if a1 < 0 or a2 < 0 or a1 < a2:
        return 0
    if a1 == 0 or a2 == 0:
        return 1
    v1 = factorial(a1) % a3
    v2 = factorial(a2) % a3
    v3 = factorial(a1 - a2) % a3
    return v1 * pow(v2, a3 - 2, a3) * pow(v3, a3 - 2, a3) % a3
v7 = f1(v1 * v2 - 2, v3 - 2, v4)
v8 = v2 ** 2 * ((v1 - 1) * v1 * (v1 + 1)) // 6
v9 = v1 ** 2 * ((v2 - 1) * v2 * (v2 + 1)) // 6
print(v7 * (v8 + v9) % v4)
