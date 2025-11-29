class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        kids = 0
        ptr = 0
        for size in s:
            if ptr < len(g) and size >= g[ptr]:
                kids += 1
                ptr += 1
        return kids
