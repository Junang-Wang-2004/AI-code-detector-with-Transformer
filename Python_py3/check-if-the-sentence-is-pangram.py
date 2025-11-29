# Time:  O(n)
# Space: O(26) = O(1)

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        """
        return len(set(sentence)) == 26
