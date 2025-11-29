import collections

class C1(object):

    def replaceWords(self, a1, a2):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a1:
            reduce(dict.__getitem__, v3, v2).setdefault('_end')

        def replace(a1):
            v1 = v2
            for v2, v3 in enumerate(a1):
                if v3 not in v1:
                    break
                v1 = v1[v3]
                if '_end' in v1:
                    return a1[:v2 + 1]
            return a1
        return ' '.join(map(replace, a2.split()))
