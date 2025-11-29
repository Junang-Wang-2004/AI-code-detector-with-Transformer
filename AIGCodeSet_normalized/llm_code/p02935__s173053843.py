v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort(reverse=True)
while len(v2) > 1:
    v2.append((v2.pop() + v2.pop()) / 2)
    v2.sort(reverse=True)
print(v2[0])
