import collections

class C1:

    def majorityFrequencyGroup(self, a1):
        v1 = {}
        v2 = []
        for v3 in a1:
            if v3 not in v1:
                v2.append(v3)
            v1[v3] = v1.get(v3, 0) + 1
        v4 = collections.Counter(v1.values())
        v5 = -1
        v6 = -1
        for v7, v8 in v4.items():
            if v8 > v5 or (v8 == v5 and v7 > v6):
                v5 = v8
                v6 = v7
        v9 = [v3 for v3 in v2 if v1[v3] == v6]
        return ''.join(v9)
