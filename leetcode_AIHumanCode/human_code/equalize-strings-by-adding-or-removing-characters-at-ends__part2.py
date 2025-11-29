# Time:  O(n * m)
# Space: O(1)
# dp
class Solution2(object):
    def minOperations(self, initial, target):
        """
        """
        result = 0
        for k in range(2):
            for i in range(k, len(initial)):
                curr = 0
                for j in range(min(len(initial)-i, len(target))):
                    curr = curr+1 if initial[i+j] == target[j] else 0
                    result = max(result, curr)
            initial, target = target, initial
        return len(initial)+len(target)-2*result


