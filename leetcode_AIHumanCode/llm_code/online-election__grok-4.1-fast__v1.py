from collections import Counter
import bisect

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.vote_times = times
        self.leader_at = []
        cnt = Counter()
        cur_leader = -1
        max_votes = 0
        for p in persons:
            cnt[p] += 1
            if cnt[p] > max_votes:
                max_votes = cnt[p]
                cur_leader = p
            elif cnt[p] == max_votes:
                cur_leader = p
            self.leader_at.append(cur_leader)

    def q(self, t):
        idx = bisect.bisect_right(self.vote_times, t) - 1
        return self.leader_at[idx]
