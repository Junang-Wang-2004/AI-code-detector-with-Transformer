class Solution(object):
    def minimumRecolors(self, blocks, k):
        prefix = [0] * (len(blocks) + 1)
        for i in range(len(blocks)):
            prefix[i + 1] = prefix[i] + (blocks[i] == 'W')
        ans = k
        for start in range(len(blocks) - k + 1):
            ans = min(ans, prefix[start + k] - prefix[start])
        return ans
