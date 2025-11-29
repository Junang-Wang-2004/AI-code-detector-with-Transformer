import collections

class C1(object):

    def watchedVideosByFriends(self, a1, a2, a3, a4):
        """
        """
        v1, v2 = (set([a3]), set([a3]))
        for v3 in range(a4):
            v1 = set((j for v4 in v1 for v5 in a2[v4] if v5 not in v2))
            v2 |= v1
        v6 = collections.Counter([v for v4 in v1 for v7 in a1[v4]])
        return sorted(list(v6.keys()), key=lambda x: (v6[x], x))
