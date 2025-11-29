v1 = 'abcdefghijklmnopqrstuvwxyz'
v2, v3 = map(int, input().split())
v4 = [list(input()) for v5 in range(v2)]
v6 = [0] * 26
for v7 in v4:
    for v8 in v7:
        v6[v1.index(v8)] += 1
v9, v10, v11 = (v2 // 2 * (v3 // 2), v2 % 2 * (v3 // 2) + v2 // 2 * (v3 % 2), v2 % 2 * (v3 % 2))
for v7 in v6:
    v8 = v7
    while v9 and v8 > 3:
        v9 -= 1
        v8 -= 4
    while v10 and v8 > 1:
        v10 -= 1
        v8 -= 2
    v11 -= v8
if not v9 == v10 == v11 == 0:
    print('No')
else:
    print('Yes')
'#一例出力、問題誤読して実装した\nc=[w*[0]for _ in range(h)]\nfi=ti=0\nfor i in range(27):\n  while b[i]:\n    if b[i]>=4:\n      j,k=fi//(w//2),fi%(w//2)\n      c[j][k]=c[j][w-k-1]=c[h-j-1][k]=c[h-j-1][w-k-1]=t[i]\n      fi+=1\n      b[i]-=4\n    if b[i]==2:\n      if ti<h//2 and w%2:c[ti][w//2]=c[h-ti-1][w//2]=t[i]\n      else:c[h//2][ti]=c[h//2][w-1-ti]=t[i]\n      ti+=1\n      b[i]-=2\n    if b[i]==1:\n      c[h//2][w//2]=t[i]\n      b[i]-=1\nfor i in c:print("".join(i))\n'
