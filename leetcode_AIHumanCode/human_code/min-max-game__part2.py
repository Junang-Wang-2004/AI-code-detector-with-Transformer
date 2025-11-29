# Time:  O(n)
# Space: O(n)
# simulation
class Solution2(object):
    def minMaxGame(self, nums):
        """
        """
        q = nums[:]
        while len(q) != 1:
            new_q = []
            for i in range(len(q)//2):
                new_q.append(min(q[2*i], q[2*i+1]) if i%2 == 0 else max(q[2*i], q[2*i+1]))
            q = new_q
        return q[0]
