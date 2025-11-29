class C1(object):

    def compareVersion(self, a1, a2):
        """
        """
        v1, v2 = (a1.split('.'), a2.split('.'))
        if len(v1) > len(v2):
            v2 += ['0' for v3 in range(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for v3 in range(len(v2) - len(v1))]
        v4 = 0
        while v4 < len(v1):
            if int(v1[v4]) > int(v2[v4]):
                return 1
            elif int(v1[v4]) < int(v2[v4]):
                return -1
            else:
                v4 += 1
        return 0

    def compareVersion2(self, a1, a2):
        """
        """
        v1 = [int(x) for v2 in a1.split('.')]
        v3 = [int(v2) for v2 in a2.split('.')]
        while len(v1) != len(v3):
            if len(v1) > len(v3):
                v3.append(0)
            else:
                v1.append(0)
        return cmp(v1, v3)

    def compareVersion3(self, a1, a2):
        v1 = (list(map(int, v.split('.'))) for v2 in (a1, a2))
        return cmp(*list(zip(*itertools.zip_longest(*v1, fillvalue=0))))

    def compareVersion4(self, a1, a2):
        v1, v2, v3 = ('0' + a1).partition('.')
        v4, v2, v5 = ('0' + a2).partition('.')
        return cmp(int(v1), int(v4)) or (len(v3 + v5) and self.compareVersion4(v3, v5))
