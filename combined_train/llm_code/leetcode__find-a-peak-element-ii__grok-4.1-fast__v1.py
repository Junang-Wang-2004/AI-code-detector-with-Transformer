class C1:

    def findPeakGrid(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        if v1 > v2:
            v3 = 0
            v4 = v1 - 1
            while v3 < v4:
                v5 = (v3 + v4) // 2
                if max(a1[v5]) > max(a1[v5 + 1]):
                    v4 = v5
                else:
                    v3 = v5 + 1
            v6 = v3
            v7 = a1[v6][0]
            v8 = 0
            for v9 in range(1, v2):
                if a1[v6][v9] > v7:
                    v7 = a1[v6][v9]
                    v8 = v9
            return [v6, v8]
        else:

            def colmax(a1):
                v1 = a1[0][a1]
                for v2 in range(1, v1):
                    if a1[v2][a1] > v1:
                        v1 = a1[v2][a1]
                return v1
            v3 = 0
            v4 = v2 - 1
            while v3 < v4:
                v5 = (v3 + v4) // 2
                if colmax(v5) > colmax(v5 + 1):
                    v4 = v5
                else:
                    v3 = v5 + 1
            v8 = v3
            v7 = a1[0][v8]
            v6 = 0
            for v10 in range(1, v1):
                if a1[v10][v8] > v7:
                    v7 = a1[v10][v8]
                    v6 = v10
            return [v6, v8]
