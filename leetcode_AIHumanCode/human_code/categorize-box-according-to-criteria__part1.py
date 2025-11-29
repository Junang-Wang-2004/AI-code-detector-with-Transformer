# Time:  O(1)
# Space: O(1)

# math, implementation
class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        """
        bulky = any(x >= 10**4 for x in (length, width, height)) or length*width*height >= 10**9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"


