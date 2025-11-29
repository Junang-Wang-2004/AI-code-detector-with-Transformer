class Solution:
    def reversePairs(self, nums):
        def helper(seq):
            if len(seq) < 2:
                return 0, seq
            half = len(seq) // 2
            lcount, lsorted = helper(seq[:half])
            rcount, rsorted = helper(seq[half:])
            pairs = 0
            ptr = 0
            for val in lsorted:
                while ptr < len(rsorted) and val > 2 * rsorted[ptr]:
                    ptr += 1
                pairs += ptr
            result = []
            x, y = 0, 0
            while x < len(lsorted) and y < len(rsorted):
                if lsorted[x] <= rsorted[y]:
                    result.append(lsorted[x])
                    x += 1
                else:
                    result.append(rsorted[y])
                    y += 1
            result.extend(lsorted[x:])
            result.extend(rsorted[y:])
            return lcount + rcount + pairs, result

        return helper(nums)[0]
