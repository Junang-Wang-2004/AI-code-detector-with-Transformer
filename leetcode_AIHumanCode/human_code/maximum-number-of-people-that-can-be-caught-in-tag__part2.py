# Time:  O(n)
# Space: O(1)
# greedy with sliding window solution
class Solution2(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        """
        result = j = 0
        for i in range(len(team)):
            if not team[i]:
                continue
            while j < i-dist:
                j += 1
            while j <= min(i+dist, len(team)-1):
                if team[j] == 0:
                    break
                j += 1
            if j <= min(i+dist, len(team)-1):
                result += 1
                j += 1
        return result
