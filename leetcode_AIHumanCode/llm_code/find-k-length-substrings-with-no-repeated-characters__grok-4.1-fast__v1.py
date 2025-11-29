class Solution:
    def numKLenSubstrNoRepeats(self, S, K):
        count = 0
        start = 0
        last_pos = {}
        for end in range(len(S)):
            if S[end] in last_pos and last_pos[S[end]] >= start:
                start = last_pos[S[end]] + 1
            last_pos[S[end]] = end
            if end - start + 1 >= K:
                count += 1
        return count
