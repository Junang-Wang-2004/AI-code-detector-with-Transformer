#abc080d

N,C=map(int,raw_input().split())
l=[[0 for i in xrange(C)] for j in xrange(10**5)]
for i in xrange(N):
 s,t,c=map(int,raw_input().split())
 s-=1
 for j in xrange(s,t):
  l[j][c-1]=1

res=0
for i in xrange(10**5):
 if sum(l[i])>res:
  res=sum(l[i])
print res
