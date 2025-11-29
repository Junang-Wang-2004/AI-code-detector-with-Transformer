# Time:  O(n)
# Space: O(n)
# string
class Solution2(object):
    def generateTag(self, caption):
        """
        """
        L = 100
        return ('#'+"".join(x.lower() if i == 0 else x[0].upper()+x[1:].lower() for i, x in enumerate(caption.split())))[:L]
