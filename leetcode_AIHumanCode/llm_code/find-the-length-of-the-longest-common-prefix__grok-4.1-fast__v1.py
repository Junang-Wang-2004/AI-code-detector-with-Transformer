class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        root = {}
        for val in arr1:
            current = root
            for digit in str(val):
                if digit not in current:
                    current[digit] = {}
                current = current[digit]
        maximum = 0
        for val in arr2:
            current = root
            length = 0
            for digit in str(val):
                if digit not in current:
                    break
                current = current[digit]
                length += 1
            maximum = max(maximum, length)
        return maximum
