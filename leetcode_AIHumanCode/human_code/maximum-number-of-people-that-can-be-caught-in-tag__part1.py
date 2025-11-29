# Time:  O(n)
# Space: O(1)

# greedy with two pointers solution
class Solution(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        """
        result = i = j = 0
        while i < len(team) and j < len(team):
            if i+dist < j or team[i] != 1:
                i += 1
            elif j+dist < i or team[j] != 0:
                j += 1
            else:
                result += 1
                i += 1
                j += 1
        return result


