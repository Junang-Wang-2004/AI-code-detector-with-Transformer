import collections
import functools

class C1(object):

    def boldWords(self, a1, a2):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3, v4 in enumerate(a1):
            functools.reduce(dict.__getitem__, v4, v2).setdefault('_end')
        v5 = [False] * len(a2)
        for v3 in range(len(a2)):
            v6 = v2
            v7 = -1
            for v8 in range(v3, len(a2)):
                if a2[v8] not in v6:
                    break
                v6 = v6[a2[v8]]
                if '_end' in v6:
                    v7 = v8
            for v8 in range(v3, v7 + 1):
                v5[v8] = True
        v9 = []
        for v3 in range(len(a2)):
            if v5[v3] and (v3 == 0 or not v5[v3 - 1]):
                v9.append('<b>')
            v9.append(a2[v3])
            if v5[v3] and (v3 == len(a2) - 1 or not v5[v3 + 1]):
                v9.append('</b>')
        return ''.join(v9)
