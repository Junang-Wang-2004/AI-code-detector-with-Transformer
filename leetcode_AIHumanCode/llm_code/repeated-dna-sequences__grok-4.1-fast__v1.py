class Solution:
    def findRepeatedDnaSequences(self, s):
        seen_once = set()
        duplicates = set()
        for i in range(len(s) - 9):
            segment = s[i:i + 10]
            if segment in seen_once:
                duplicates.add(segment)
            seen_once.add(segment)
        return list(duplicates)
