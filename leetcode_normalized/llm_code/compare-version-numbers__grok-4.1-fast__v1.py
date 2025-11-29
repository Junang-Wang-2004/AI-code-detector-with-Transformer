class C1(object):

    def compareVersion(self, a1, a2):
        v1 = list(map(int, a1.split('.')))
        v2 = list(map(int, a2.split('.')))
        v3 = 0
        while v3 < len(v1) or v3 < len(v2):
            v4 = v1[v3] if v3 < len(v1) else 0
            v5 = v2[v3] if v3 < len(v2) else 0
            if v4 < v5:
                return -1
            if v4 > v5:
                return 1
            v3 += 1
        return 0
