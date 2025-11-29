def f1(a1, a2):
    for v1 in range(len(a1)):
        for v2 in range(len(a1[v1])):
            a2[v1][v2] = False
    for v1 in range(len(a1)):
        for v2 in range(len(a1[v1])):
            if a1[v1][v2]:
                for v3 in range(v1 + 1, len(a1)):
                    if not a1[v3][v2]:
                        a2[v1][v2] = True
                        break
                if not a2[v1][v2]:
                    for v3 in range(v2 + 1, len(a1[v1])):
                        if not a1[v1][v3]:
                            a2[v1][v2] = True
                            break
    for v1 in range(len(a2)):
        for v2 in range(len(a2[v1])):
            if a2[v1][v2]:
                print(v1, v2, 'contains a strawberry')
