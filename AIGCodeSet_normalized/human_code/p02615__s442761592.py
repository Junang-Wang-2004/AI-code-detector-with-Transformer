n=input()
a=[int(i) for i in raw_input().split()]
a.sort()
s=a[n-1]
for i in range(n/2,n-1):
  s+=a[i]*2
if(n%2==1):
  s-=a[n/2]
print s
