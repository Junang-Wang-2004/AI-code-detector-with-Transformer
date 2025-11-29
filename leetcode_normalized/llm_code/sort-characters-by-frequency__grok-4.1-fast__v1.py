class C1(object):

    def frequencySort(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = sorted(v1, key=v1.get, reverse=True)
        return ''.join((v2 * v1[v2] for v2 in v3))
