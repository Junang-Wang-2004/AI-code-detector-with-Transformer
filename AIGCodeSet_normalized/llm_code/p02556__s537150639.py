def f1():
    v1 = int(input())
    v2 = []
    for v3 in range(v1):
        v4, v5 = [int(a) for v6 in input().split(' ')]
        v2.append({'x': v4, 'y': v5})
    v2.sort(key=lambda z: z['x'])
    v7 = v2[1]['x'] - v2[0]['x']
    v8 = v2[-1]['x'] - v2[0]['x']
    v2.sort(key=lambda z: z['y'])
    v9 = v2[1]['y'] - v2[0]['y']
    v10 = v2[-1]['y'] - v2[0]['y']
    print(max(v8, v10, v7, v9))
f1()
