import collections

class C1(object):

    def subdomainVisits(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v3, v2 = v2.split()
            v3 = int(v3)
            v4 = v2.split('.')
            v5 = []
            for v6 in reversed(range(len(v4))):
                v5.append(v4[v6])
                v1['.'.join(reversed(v5))] += v3
        return ['{} {}'.format(v3, v2) for v2, v3 in v1.items()]
