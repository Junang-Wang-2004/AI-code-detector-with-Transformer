# Time:  O(n)
# Space: O(n)
# prefix sum, greedy
class Solution2(object):
    def minMoves(self, rooks):
        """
        """
        def count(arr):
            cnt = [0]*len(arr)
            for x in arr:
                cnt[x] += 1
            result = bal = 0
            for i in range(len(rooks)):
                bal += cnt[i]-1
                result += abs(bal)
            return result

        return sum(count(arr) for arr in zip(*rooks))
    
