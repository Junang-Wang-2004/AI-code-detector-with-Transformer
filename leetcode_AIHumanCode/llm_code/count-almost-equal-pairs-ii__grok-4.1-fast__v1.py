from collections import Counter

class Solution:
    def countPairs(self, nums):
        N_DIGITS = 7
        powers = [1]
        for _ in range(N_DIGITS - 1):
            powers.append(powers[-1] * 10)
        
        def neighbors(val):
            nbrs = []
            for i in range(N_DIGITS):
                for j in range(i + 1, N_DIGITS):
                    d1 = (val // powers[i]) % 10
                    d2 = (val // powers[j]) % 10
                    if d1 == d2:
                        continue
                    delta = (d2 - d1) * (powers[i] - powers[j])
                    nbrs.append(val + delta)
            return nbrs
        
        def get_reachable(val):
            rset = {val}
            n1 = neighbors(val)
            rset.update(n1)
            for mid in n1:
                for ext in neighbors(mid):
                    rset.add(ext)
            return list(rset)
        
        freq = Counter(nums)
        prefix_sum = Counter()
        answer = 0
        for num in list(freq):
            f = freq[num]
            answer += prefix_sum[num] * f + f * (f - 1) // 2
            reachable = get_reachable(num)
            for r in reachable:
                prefix_sum[r] += f
        return answer
