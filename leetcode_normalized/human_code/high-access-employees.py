import collections

class C1(object):

    def findHighAccessEmployees(self, a1):
        """
        """
        v1 = 2
        v2 = 60

        def to_minute(a1):
            return int(a1[:2]) * 60 + int(a1[2:])
        v3 = collections.defaultdict(list)
        for v4, v5 in a1:
            v3[v4].append(to_minute(v5))
        v6 = []
        for v4, v7 in v3.items():
            v7.sort()
            if not all((v7[i] + v2 <= v7[i + v1] for v8 in range(len(v7) - v1))):
                v6.append(v4)
        return v6
