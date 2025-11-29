# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def plusOne(self, digits):
        """
        """
        result = digits[::-1]
        carry = 1
        for i in range(len(result)):
            result[i] += carry
            carry, result[i] = divmod(result[i], 10)
        if carry:
            result.append(carry)
        return result[::-1]


