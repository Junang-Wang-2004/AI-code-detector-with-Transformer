# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def arrangeWords(self, text):
        """
        """
        result = text.split()
        result[0] = result[0].lower()
        result.sort(key=len) 
        result[0] = result[0].title()
        return " ".join(result)
