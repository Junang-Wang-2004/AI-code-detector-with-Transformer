
import sys

N=input()
V=map(int, sys.stdin.readline().split())
C=map(int, sys.stdin.readline().split())

ans=0
for v,c in zip(V,C):
    if v>=c:
        ans+=v-c

print ans
