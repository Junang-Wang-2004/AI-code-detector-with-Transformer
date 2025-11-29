class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        words1 = sentence1.split()
        words2 = sentence2.split()
        len1, len2 = len(words1), len(words2)
        pref = 0
        while pref < min(len1, len2) and words1[pref] == words2[pref]:
            pref += 1
        suff = 0
        while suff < min(len1, len2) and words1[len1 - 1 - suff] == words2[len2 - 1 - suff]:
            suff += 1
        return pref + suff >= min(len1, len2)
