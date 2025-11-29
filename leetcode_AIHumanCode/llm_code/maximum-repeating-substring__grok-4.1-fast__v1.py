class Solution(object):
    def maxRepeating(self, sequence, word):
        if len(sequence) < len(word):
            return 0
        max_cnt = 0
        start = 0
        while True:
            start = sequence.find(word, start)
            if start == -1:
                break
            cnt = 1
            pos = start + len(word)
            while pos + len(word) <= len(sequence) and sequence[pos:pos + len(word)] == word:
                cnt += 1
                pos += len(word)
            max_cnt = max(max_cnt, cnt)
            start = pos
        return max_cnt
