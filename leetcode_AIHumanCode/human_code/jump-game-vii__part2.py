# Time:  O(n)
# Space: O(n)
import collections


# bfs solution
class Solution2(object):
    def canReach(self, s, minJump, maxJump):
        """
        """
        q = collections.deque([0])
        reachable = 0
        while q:
            i = q.popleft()
            for j in range(max(i+minJump, reachable+1), min(i+maxJump+1, len(s))):
                if s[j] != '0':
                    continue
                q.append(j)
            reachable = i+maxJump
        return i == len(s)-1
