# Time:  O(n)
# Space: O(n)

# backward simulation, doubly linked list
class Solution(object):
    def minTime(self, s, order, k):
        """
        """
        left = list(range(-1, len(s)-1))
        right = list(range(1, len(s)+1))
        cnt = (len(s)+1)*len(s)//2
        if cnt < k:
            return -1
        for t in reversed(range(len(order))):
            i = order[t]
            l = left[i]
            r = right[i]
            cnt -= (i-l)*(r-i)
            if cnt < k:
                break
            if l >= 0:
                right[l] = r
            if r < len(left):
                left[r] = l
        return t
