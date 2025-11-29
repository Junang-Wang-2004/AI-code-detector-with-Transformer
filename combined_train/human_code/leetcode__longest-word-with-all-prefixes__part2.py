import collections
import string

class C1(object):

    def longestWord(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            if a3[0] == -1 or len(a1[a2['_end']]) > len(a1[a3[0]]):
                a3[0] = a2['_end']
            for v1 in string.ascii_lowercase:
                if v1 not in a2 or '_end' not in a2[v1]:
                    continue
                dfs(a1, a2[v1], a3)
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v2['_end'] = -1
        for v3, v4 in enumerate(a1):
            reduce(dict.__getitem__, v4, v2)['_end'] = v3
        v5 = [-1]
        dfs(a1, v2, v5)
        return a1[v5[0]] if v5[0] != -1 else ''
