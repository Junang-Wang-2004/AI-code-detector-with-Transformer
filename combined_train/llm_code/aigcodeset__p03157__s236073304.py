def f1(a1, a2, a3, a4, a5):
    v1 = 0
    "\n    if current_h in search_map:\n        search_map[current_h]\n    else:\n        search_map[current_h] = {}\n        search_map[current_h][current_w] = True\n    search_map[current_h][current_w] = True\n    current = s_map[current_h][current_w]\n    if (current == '.'):\n        num += 1\n    else:\n        group[current_h][current_w] = group_index\n    # 上\n    if current_h != 0:\n        next_h = current_h-1\n        next_w = current_w\n        isExist = False\n        if next_h in search_map:\n            if next_w in search_map[next_h]:\n                isExist = True\n        if s_map[next_h][next_w] != current and not(isExist):\n            num += search(search_map, group, next_h, next_w, group_index)\n    # 下\n    if current_h < H-1:\n        next_h = current_h+1\n        next_w = current_w\n        isExist = False\n        if next_h in search_map:\n            if next_w in search_map[next_h]:\n                isExist = True\n        if s_map[next_h][next_w] != current and not(isExist):\n            num += search(search_map, group, next_h, next_w, group_index)\n    # 左\n    if current_w != 0:\n        next_h = current_h\n        next_w = current_w-1\n        isExist = False\n        if next_h in search_map:\n            if next_w in search_map[next_h]:\n                isExist = True\n        if s_map[next_h][next_w] != current and not(isExist):\n            num += search(search_map, group, next_h, next_w, group_index)\n    # 右\n    if current_w < W-1:\n        next_h = current_h\n        next_w = current_w+1\n        isExist = False\n        if next_h in search_map:\n            if next_w in search_map[next_h]:\n                isExist = True\n        if s_map[next_h][next_w] != current and not(isExist):\n            num += search(search_map, group, next_h, next_w, group_index)\n    "
    return v1
v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v5 = {}
v6 = {}
v7 = {}
for v8 in range(v1):
    v5[v8] = {}
    v6[v8] = {}
    v9 = list(v3[v8])
    for v10 in range(v2):
        v5[v8][v10] = v9[v10]
        v6[v8][v10] = 0
v11 = 0
v12 = 1
v13 = {}
v13[0] = 0
for v8 in range(v1):
    for v10 in range(v2):
        if v5[v8][v10] == '#':
            if v6[v8][v10] != 0:
                v11 += v13[v6[v8][v10]]
            else:
                v14 = f1(v7, v6, v8, v10, v12)
                v13[v12] = v14
                v12 += 1
                v11 += v14
print(v11)
