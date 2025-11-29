class C1:

    def findCircleNum(self, a1):
        v1 = len(a1)
        v2 = [False] * v1

        def explore(a1):
            v1 = [a1]
            v2[a1] = True
            while v1:
                v2 = v1.pop()
                for v3 in range(v1):
                    if a1[v2][v3] and (not v2[v3]):
                        v2[v3] = True
                        v1.append(v3)
        v3 = 0
        for v4 in range(v1):
            if not v2[v4]:
                explore(v4)
                v3 += 1
        return v3
