class Solution:
    def findLongestWord(self, s, d):
        ans = ""
        for candidate in d:
            pos = 0
            valid = True
            for letter in candidate:
                pos = s.find(letter, pos)
                if pos == -1:
                    valid = False
                    break
                pos += 1
            if valid and (len(candidate) > len(ans) or (len(candidate) == len(ans) and candidate < ans)):
                ans = candidate
        return ans
