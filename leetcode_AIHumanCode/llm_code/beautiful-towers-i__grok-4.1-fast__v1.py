class Solution:
    def maximumSumOfHeights(self, maxHeights):
        n = len(maxHeights)
        prefix = [0] * n
        st = [-1]
        sm = 0
        for i in range(n):
            while len(st) > 1 and maxHeights[st[-1]] >= maxHeights[i]:
                p = st.pop()
                sm -= (p - st[-1]) * maxHeights[p]
            sm += (i - st[-1]) * maxHeights[i]
            st.append(i)
            prefix[i] = sm
        suffix = [0] * n
        st = [n]
        sm = 0
        for i in range(n - 1, -1, -1):
            while len(st) > 1 and maxHeights[st[-1]] >= maxHeights[i]:
                p = st.pop()
                sm -= (st[-1] - p) * maxHeights[p]
            sm += (st[-1] - i) * maxHeights[i]
            st.append(i)
            suffix[i] = sm
        res = 0
        for i in range(n):
            res = max(res, prefix[i] + suffix[i] - maxHeights[i])
        return res
