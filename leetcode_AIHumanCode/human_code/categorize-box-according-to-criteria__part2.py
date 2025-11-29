# Time:  O(1)
# Space: O(1)
# math, implementation
class Solution2(object):
    def categorizeBox(self, length, width, height, mass):
        """
        """
        CATEGORIES = ["Neither", "Heavy", "Bulky", "Both"]
        i = 2*(any(x >= 10**4 for x in (length, width, height)) or length*width*height >= 10**9)+int(mass >= 100)
        return CATEGORIES[i]
