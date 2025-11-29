import collections

class C1:

    def findDuplicate(self, a1):
        v1 = collections.defaultdict(list)
        for v2 in a1:
            v3 = v2.split()
            v4 = v3[0]
            for v5 in v3[1:]:
                v6, v7 = v5.split('(', 1)
                v8, v9 = v7.split(')', 1)
                v1[v8].append(f'{v4}/{v6}')
        return [group for v10 in v1.values() if len(v10) > 1]
