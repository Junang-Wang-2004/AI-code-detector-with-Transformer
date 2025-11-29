# Time:  O(n)
# Space: O(1)

# string
class Solution(object):
    def generateTag(self, caption):
        """
        """
        L = 100
        result = ['#']
        for i in range(len(caption)):
            if caption[i] == ' ':
                continue
            result.append(caption[i].upper() if i == 0 or caption[i-1] == ' ' else caption[i].lower())
            if len(result) == L:
                break
        if 1 < len(result):
            result[1] = result[1].lower()
        return "".join(result)


