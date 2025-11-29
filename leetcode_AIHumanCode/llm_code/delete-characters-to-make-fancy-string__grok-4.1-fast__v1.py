class Solution(object):
    def makeFancyString(self, s):
        result = []
        for char in s:
            if len(result) >= 2 and result[-1] == result[-2] == char:
                continue
            result.append(char)
        return ''.join(result)
