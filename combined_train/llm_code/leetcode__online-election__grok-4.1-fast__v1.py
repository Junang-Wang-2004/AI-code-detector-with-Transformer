from collections import Counter
import bisect

class C1(object):

    def __init__(self, a1, a2):
        self.vote_times = a2
        self.leader_at = []
        v1 = Counter()
        v2 = -1
        v3 = 0
        for v4 in a1:
            v1[v4] += 1
            if v1[v4] > v3:
                v3 = v1[v4]
                v2 = v4
            elif v1[v4] == v3:
                v2 = v4
            self.leader_at.append(v2)

    def q(self, a1):
        v1 = bisect.bisect_right(self.vote_times, a1) - 1
        return self.leader_at[v1]
