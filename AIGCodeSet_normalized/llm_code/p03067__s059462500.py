v1, v2, v3 = map(int, input().split())
v4 = 'Yes' if min(v1, v2) <= v3 <= max(v1, v2) else 'No'
print(v4)
