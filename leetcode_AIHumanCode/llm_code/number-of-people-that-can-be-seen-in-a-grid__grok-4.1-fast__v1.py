class Solution:
    def seePeople(self, heights):
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        ans = [[0] * n for _ in range(m)]

        def right_vis(line):
            sz = len(line)
            res = [0] * sz
            st = []
            for idx in range(sz - 1, -1, -1):
                ht = line[idx]
                num = 0
                while st and st[-1] < ht:
                    st.pop()
                    num += 1
                if st:
                    num += 1
                if not st or st[-1] != ht:
                    st.append(ht)
                res[idx] = num
            return res

        for x in range(m):
            rvis = right_vis(heights[x])
            for y in range(n):
                ans[x][y] += rvis[y]

        for y in range(n):
            cl = [heights[x][y] for x in range(m)]
            cvis = right_vis(cl)
            for x in range(m):
                ans[x][y] += cvis[x]

        return ans
