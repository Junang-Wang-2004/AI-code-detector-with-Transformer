class Solution:
    def kIncreasing(self, arr, k):
        def nondec_lis_length(seq):
            pile_tops = []
            for val in seq:
                idx = 0
                while idx < len(pile_tops) and pile_tops[idx] <= val:
                    idx += 1
                if idx == len(pile_tops):
                    pile_tops.append(val)
                else:
                    pile_tops[idx] = val
            return len(pile_tops)

        total = len(arr)
        salvage = 0
        for offset in range(k):
            chain = arr[offset::k]
            salvage += nondec_lis_length(chain)
        return total - salvage
