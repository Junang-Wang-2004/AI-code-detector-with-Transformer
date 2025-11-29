# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        """
        cols = len(encodedText)//rows
        result = []
        for i in range(cols):
            for j in range(i, len(encodedText), cols+1):
                result.append(encodedText[j])
        while result and result[-1] == ' ':
            result.pop()
        return "".join(result)

