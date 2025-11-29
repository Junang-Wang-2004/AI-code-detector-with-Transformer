class Solution(object):
    def recoverArray(self, arr):
        arr.sort()
        half = len(arr) // 2
        counts = {}
        for val in arr:
            counts[val] = counts.get(val, 0) + 1
        for pos in range(1, half + 1):
            gap = arr[pos] - arr[0]
            if gap == 0 or gap % 2 != 0:
                continue
            diff = gap // 2
            freq_copy = counts.copy()
            ans = []
            good = True
            for elem in arr:
                if freq_copy.get(elem, 0) == 0:
                    continue
                mate = elem + 2 * diff
                if freq_copy.get(mate, 0) == 0:
                    good = False
                    break
                freq_copy[elem] -= 1
                freq_copy[mate] -= 1
                ans.append(elem + diff)
            if good:
                return ans
        return []
