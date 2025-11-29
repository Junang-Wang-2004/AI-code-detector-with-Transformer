class Solution(object):
    def oddString(self, words):
        patterns = {}
        n = len(words[0]) - 1
        for term in words:
            key = ','.join(str(ord(term[j + 1]) - ord(term[j])) for j in range(n))
            patterns.setdefault(key, []).append(term)
        for candidates in patterns.values():
            if len(candidates) == 1:
                return candidates[0]
