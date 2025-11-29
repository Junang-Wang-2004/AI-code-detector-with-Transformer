import collections

class C1(object):

    def majorityFrequencyGroup(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        v3 = collections.defaultdict(list)
        for v2, v4 in v1.items():
            v3[v4].append(v2)
        v5 = max(iter(v3.keys()), key=lambda x: (len(v3[v2]), v2))
        return ''.join(v3[v5])
