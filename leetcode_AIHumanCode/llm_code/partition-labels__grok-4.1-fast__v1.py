class Solution:
    def partitionLabels(self, S):
        n = len(S)
        last_idx = [-1] * 26
        pos = n - 1
        while pos >= 0:
            c_idx = ord(S[pos]) - ord('a')
            if last_idx[c_idx] == -1:
                last_idx[c_idx] = pos
            pos -= 1
        ans = []
        start_pos = 0
        max_reach = 0
        pos = 0
        while pos < n:
            max_reach = max(max_reach, last_idx[ord(S[pos]) - ord('a')])
            if pos == max_reach:
                ans.append(pos - start_pos + 1)
                start_pos = pos + 1
            pos += 1
        return ans
