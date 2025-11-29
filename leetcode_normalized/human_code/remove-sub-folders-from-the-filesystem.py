import collections
import itertools

class C1(object):

    def removeSubfolders(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            if '_end' in a1:
                a3.append('/' + '/'.join(a2))
                return
            for v1 in a1:
                if v1 == '_end':
                    continue
                a2.append(v1)
                dfs(a1[v1], a2, a3)
                a2.pop()
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a1:
            v4 = v3.split('/')
            reduce(dict.__getitem__, itertools.islice(v4, 1, len(v4)), v2).setdefault('_end')
        v5 = []
        dfs(v2, [], v5)
        return v5
