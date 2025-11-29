v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort(reverse=True)
print(sum(v2) - v2[-1])
