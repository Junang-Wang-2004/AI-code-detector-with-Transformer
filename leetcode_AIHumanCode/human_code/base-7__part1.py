# Time:  O(1)
# Space: O(1)

class Solution(object):
    def convertToBase7(self, num):
        if num < 0:
            return '-' + self.convertToBase7(-num)
        result = ''
        while num:
            result = str(num % 7) + result
            num //= 7
        return result if result else '0'


