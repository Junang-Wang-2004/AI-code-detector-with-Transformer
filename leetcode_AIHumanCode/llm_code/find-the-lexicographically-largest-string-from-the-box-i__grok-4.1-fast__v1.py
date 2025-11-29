class Solution:
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        n = len(word)
        max_len = n - numFriends + 1
        best = word[:max_len]
        for start in range(1, n):
            clen = min(max_len, n - start)
            current = word[start:start + clen]
            if current > best:
                best = current
        return best
