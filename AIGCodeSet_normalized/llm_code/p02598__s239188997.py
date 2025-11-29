"""
Created on Sun Aug  2 21:11:34 2020

@author: NEC-PCuser
"""
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
while v2 > 0 and len(v3) > 1:
    v3[0] = (v3[0] + v3[1]) / 2
    v3.pop(1)
    v2 -= 1
    v3.sort()
print(int(v3[0]))
