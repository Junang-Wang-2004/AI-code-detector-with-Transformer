class C1(object):

    def largestMerge(self, a1, a2):
        v1 = []
        v2, v3 = (0, 0)
        v4, v5 = (len(a1), len(a2))
        while v2 < v4 or v3 < v5:
            v6, v7 = (v2, v3)
            while v6 < v4 and v7 < v5 and (a1[v6] == a2[v7]):
                v6 += 1
                v7 += 1
            if v6 < v4 and (v7 == v5 or a1[v6] > a2[v7]):
                v1.append(a1[v2])
                v2 += 1
            else:
                v1.append(a2[v3])
                v3 += 1
        return ''.join(v1)
