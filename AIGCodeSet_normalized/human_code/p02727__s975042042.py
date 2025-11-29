v1, v2, v3, v4, v5 = map(int, input().split())
v6 = sorted(list(map(int, input().split())))[-v1:]
v7 = sorted(list(map(int, input().split())))[-v2:]
v8 = list(map(int, input().split()))
print(sum(sorted(v6 + v7 + v8)[-(v1 + v2):]))
