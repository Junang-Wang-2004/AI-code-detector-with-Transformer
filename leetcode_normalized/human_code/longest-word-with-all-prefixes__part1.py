import collections
import string

class C1(object):

    def longestWord(self, a1):
        """
        """

        def iter_dfs(a1, a2):
            v1 = -1
            v2 = [a2]
            while v2:
                a2 = v2.pop()
                if v1 == -1 or len(a1[a2['_end']]) > len(a1[v1]):
                    v1 = a2['_end']
                for v4 in reversed(string.ascii_lowercase):
                    if v4 not in a2 or '_end' not in a2[v4]:
                        continue
                    v2.append(a2[v4])
            return v1
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v2['_end'] = -1
        for v3, v4 in enumerate(a1):
            reduce(dict.__getitem__, v4, v2)['_end'] = v3
        v5 = iter_dfs(a1, v2)
        return a1[v5] if v5 != -1 else ''
