class Solution(object):
    def countCharacters(self, words, chars):
        a_ord = ord('a')
        avail = [0] * 26
        for ch in chars:
            avail[ord(ch) - a_ord] += 1
        result = 0
        for term in words:
            need = [0] * 26
            for ch in term:
                need[ord(ch) - a_ord] += 1
            if all(need[k] <= avail[k] for k in range(26)):
                result += len(term)
        return result
