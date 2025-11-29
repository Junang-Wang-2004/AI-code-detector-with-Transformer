class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        res = []
        for lst in groups.values():
            lst.sort()
            res.append(lst)
        return res
