class Solution:
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers.sort()
        n = 0
        while n < len(flowers) and flowers[n] < target:
            n += 1
        pre = [0]
        for i in range(n):
            pre.append(pre[-1] + flowers[i])
        ans = 0
        sufsum = pre[-1]
        ptr = 0
        m = len(flowers)
        for cnt in range(n + 1):
            if cnt:
                sufsum -= flowers[cnt - 1]
            req = (n - cnt) * target - sufsum
            extra = newFlowers - req
            if extra < 0:
                continue
            while ptr < cnt and (ptr == 0 or (extra + pre[ptr]) // ptr > flowers[ptr]):
                ptr += 1
            height = min((extra + pre[ptr]) // ptr if ptr else 0, target - 1)
            beauty = height * partial + (m - cnt) * full
            if beauty > ans:
                ans = beauty
        return ans
