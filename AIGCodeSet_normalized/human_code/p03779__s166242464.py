"""
カンガルー
時刻iで長さiのジャンプをするx-i,x,x+i
0からスタートして、座標Xにつくまでの時間
"""
v1 = int(input())
v2 = int((2 * v1) ** 0.5) + 1
v3 = v2 * (v2 + 1) // 2
if v3 - v1 >= v2:
    print(v2 - 1)
else:
    print(v2)
