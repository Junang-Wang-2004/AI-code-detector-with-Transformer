class Solution:
    def maxProduct(self, s):
        n = len(s)
        if n == 0:
            return 0

        def get_max_end_lens(st):
            t = '^#' + '#'.join(st) + '#$'
            N = len(t)
            rad = [0] * N
            ctr = rght = 0
            for i in range(1, N - 1):
                mirror = 2 * ctr - i
                if i < rght:
                    rad[i] = min(rght - i, rad[mirror])
                while t[i + rad[i] + 1] == t[i - rad[i] - 1]:
                    rad[i] += 1
                if i + rad[i] > rght:
                    ctr = i
                    rght = i + rad[i]
            maxend = [1] * n
            for k in range(n):
                cpos = 2 * k + 2
                radius = rad[cpos] // 2
                endpos = k + radius
                leng = 2 * radius + 1
                maxend[endpos] = max(maxend[endpos], leng)
            for pos in range(n - 2, -1, -1):
                maxend[pos] = max(maxend[pos], maxend[pos + 1] - 2)
            return maxend

        endmax_left = get_max_end_lens(s)
        endmax_right = get_max_end_lens(s[::-1])

        startmax = [endmax_right[n - 1 - j] for j in range(n)]

        pref = 0
        leftmx = [0]
        for j in range(n):
            pref = max(pref, endmax_left[j])
            leftmx.append(pref)

        suff = 0
        rightmx = [0] * n
        for j in range(n - 1, -1, -1):
            suff = max(suff, startmax[j])
            rightmx[j] = suff

        ans = 0
        for i in range(n):
            ans = max(ans, leftmx[i] * rightmx[i])
        return ans
