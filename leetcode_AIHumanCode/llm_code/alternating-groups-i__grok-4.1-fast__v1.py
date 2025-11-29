class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        n = len(colors)
        ans = 0
        for i in range(n):
            j = (i + 1) % n
            k = (i + 2) % n
            if colors[i] != colors[j] and colors[j] != colors[k]:
                ans += 1
        return ans
