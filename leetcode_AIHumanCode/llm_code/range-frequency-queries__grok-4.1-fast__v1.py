class RangeFreqQuery:

    def __init__(self, arr):
        self.occurrences = {}
        for idx, num in enumerate(arr):
            self.occurrences.setdefault(num, []).append(idx)

    def _find_first_ge(self, lst, target):
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def _find_first_gt(self, lst, target):
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

    def query(self, left, right, value):
        positions = self.occurrences.get(value, [])
        return self._find_first_gt(positions, right) - self._find_first_ge(positions, left)
