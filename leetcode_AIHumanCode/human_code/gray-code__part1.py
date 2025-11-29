# Time:  O(2^n)
# Space: O(1)

class Solution(object):
    def grayCode(self, n):
        """
        """
        result = [0]
        for i in range(n):
            for n in reversed(result):
                result.append(1 << i | n)
        return result


# Proof of closed form formula could be found here:
# http://math.stackexchange.com/questions/425894/proof-of-closed-form-formula-to-convert-a-binary-number-to-its-gray-code
