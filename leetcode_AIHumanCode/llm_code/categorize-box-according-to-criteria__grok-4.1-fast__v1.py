class Solution:
    def categorizeBox(self, length, width, height, mass):
        max_side = max(length, width, height)
        volume = length * width * height
        oversized = max_side >= 10000 or volume >= 1000000000
        weighty = mass >= 100
        if oversized:
            return ["Bulky", "Both"][weighty]
        return ["Neither", "Heavy"][weighty]
