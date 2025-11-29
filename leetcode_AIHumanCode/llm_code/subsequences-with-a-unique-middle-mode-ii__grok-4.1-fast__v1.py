import collections

class Solution(object):
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        def comb2(x):
            return x * (x - 1) // 2
        n = len(nums)
        cntL = collections.defaultdict(int)
        cntR = collections.defaultdict(int)
        for num in nums:
            cntR[num] += 1
        sqL = 0
        sqR = sum(c * c for c in cntR.values())
        prodLR = 0
        sqL_prodR = 0
        prodLR_sqR = 0
        res = 0
        for i in range(n):
            val = nums[i]
            sqL -= cntL[val] * cntL[val]
            sqR -= cntR[val] * cntR[val]
            prodLR -= cntL[val] * cntR[val]
            sqL_prodR -= cntL[val] * cntL[val] * cntR[val]
            prodLR_sqR -= cntL[val] * cntR[val] * cntR[val]
            cntR[val] -= 1
            leftSz = i
            rightSz = n - i - 1
            leftV = cntL[val]
            rightV = cntR[val]
            nonLV = leftSz - leftV
            nonRV = rightSz - rightV
            totalWays = comb2(leftSz) * comb2(rightSz)
            zeroExtra = comb2(nonLV) * comb2(nonRV)
            oneLeftV = leftV * nonLV * comb2(nonRV)
            oneRightV = comb2(nonLV) * rightV * nonRV
            highExtra = (totalWays - zeroExtra - oneLeftV - oneRightV) % MOD
            s2_nonL = (sqL - nonLV) // 2
            s2_nonR = (sqR - nonRV) // 2
            good1L2R = nonLV * comb2(nonRV) - nonRV * prodLR + prodLR_sqR - s2_nonR * nonLV
            good1L = (leftV * good1L2R) % MOD
            good2L1R = nonRV * comb2(nonLV) - nonLV * prodLR + sqL_prodR - s2_nonL * nonRV
            good1R = (rightV * good2L1R) % MOD
            res = (res + highExtra + good1L + good1R) % MOD
            cntL[val] += 1
            sqL += cntL[val] * cntL[val]
            sqR += cntR[val] * cntR[val]
            prodLR += cntL[val] * cntR[val]
            sqL_prodR += cntL[val] * cntL[val] * cntR[val]
            prodLR_sqR += cntL[val] * cntR[val] * cntR[val]
        return res
