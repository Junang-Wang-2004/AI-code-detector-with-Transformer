class C1:

    def largestMultipleOfThree(self, a1):
        v1 = [0] * 10
        v2 = 0
        for v3 in a1:
            v1[v3] += 1
            v2 += v3
        v4 = v2 % 3
        if v4 != 0:
            v5 = False
            for v6 in range(10):
                if v1[v6] > 0 and v6 % 3 == v4:
                    v1[v6] -= 1
                    v5 = True
                    break
            if not v5:
                for v7 in range(10):
                    if v1[v7] == 0:
                        continue
                    v8 = v7 % 3
                    v9 = (v4 - v8) % 3
                    for v10 in range(10):
                        if v7 != v10 and v1[v10] == 0:
                            continue
                        v11 = v10 % 3
                        if v11 != v9:
                            continue
                        if v7 == v10:
                            if v1[v7] >= 2:
                                v1[v7] -= 2
                                v5 = True
                                break
                        else:
                            v1[v7] -= 1
                            v1[v10] -= 1
                            v5 = True
                            break
                    if v5:
                        break
        v12 = []
        for v6 in range(9, -1, -1):
            v12.extend(str(v6) * v1[v6])
        v13 = ''.join(v12)
        return '0' if not v13 or v13[0] == '0' else v13
