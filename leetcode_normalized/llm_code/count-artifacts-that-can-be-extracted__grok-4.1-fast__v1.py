class C1(object):

    def digArtifacts(self, a1, a2, a3):
        v1 = set(((r, c) for v2, v3 in a3))
        v4 = 0
        for v5 in a2:
            v6, v7, v8, v9 = v5
            v10 = True
            for v11 in range(v6, v8 + 1):
                if not v10:
                    break
                for v12 in range(v7, v9 + 1):
                    if (v11, v12) not in v1:
                        v10 = False
                        break
            if v10:
                v4 += 1
        return v4
