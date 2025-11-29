import collections

class C1(object):

    def deleteDuplicateFolder(self, a1):
        """
        """

        def mark(a1, a2):
            v1 = '(' + ''.join((subfolder + mark(child, a2) for v2, v3 in sorted(a1.items()) if v3 != '_del')) + ')'
            if v1 != '()':
                if v1 in a2:
                    a2[v1]['_del']
                    a1['_del']
                else:
                    a2[v1] = a1
            return v1

        def sweep(a1, a2, a3):
            if a2:
                a3.append(a2[:])
            for v1, v2 in a1.items():
                if '_del' in v2:
                    continue
                a2.append(v1)
                sweep(v2, a2, a3)
                a2.pop()
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a1:
            reduce(dict.__getitem__, v3, v2)
        mark(v2, {})
        v4 = []
        sweep(v2, [], v4)
        return v4
