class C1:

    def maxDiff(self, a1):
        v1 = str(a1)
        v2 = '0'
        for v3 in range(len(v1)):
            if v1[v3] != '9':
                v2 = v1[v3]
                break
        v4 = v1.replace(v2, '9')
        v5 = '0'
        v6 = '0'
        for v3 in range(len(v1)):
            if v1[v3] > '1':
                v5 = v1[v3]
                v6 = '1' if v3 == 0 else '0'
                break
        v7 = v1.replace(v5, v6)
        return int(v4) - int(v7)
