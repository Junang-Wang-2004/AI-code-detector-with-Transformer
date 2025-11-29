class Solution:
    def stringMatching(self, words):
        n = len(words)
        matches = set()
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    matches.add(i)
                    break
        return [words[i] for i in range(n) if i in matches]
