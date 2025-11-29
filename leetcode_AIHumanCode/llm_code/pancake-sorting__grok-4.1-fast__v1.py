class Solution:
    def pancakeSort(self, arr):
        flips = []
        size = len(arr)
        for end in range(size, 1, -1):
            idx = arr[:end].index(end)
            if idx != end - 1:
                arr[:idx + 1] = arr[:idx + 1][::-1]
                flips.append(idx + 1)
                arr[:end] = arr[:end][::-1]
                flips.append(end)
        return flips
