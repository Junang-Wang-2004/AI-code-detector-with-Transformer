class Solution:
    def restoreString(self, s, indices):
        n = len(s)
        orig_pos = [0] * n
        for k, target in enumerate(indices):
            orig_pos[target] = k
        shuffled = []
        for m in range(n):
            shuffled.append(s[orig_pos[m]])
        return ''.join(shuffled)
