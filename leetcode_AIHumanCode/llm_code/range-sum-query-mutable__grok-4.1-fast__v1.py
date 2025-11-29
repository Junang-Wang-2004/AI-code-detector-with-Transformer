class NumArray:
    def __init__(self, values):
        self.length = len(values)
        self.segment = [0] * (4 * self.length)
        if self.length > 0:
            self._build_tree(1, 0, self.length - 1, values)

    def _build_tree(self, current, low, high, values):
        if low == high:
            self.segment[current] = values[low]
            return
        middle = (low + high) // 2
        self._build_tree(2 * current, low, middle, values)
        self._build_tree(2 * current + 1, middle + 1, high, values)
        self.segment[current] = self.segment[2 * current] + self.segment[2 * current + 1]

    def update(self, position, new_value):
        self._modify_tree(1, 0, self.length - 1, position, new_value)

    def _modify_tree(self, current, low, high, position, new_value):
        if low == high:
            self.segment[current] = new_value
            return
        middle = (low + high) // 2
        if position <= middle:
            self._modify_tree(2 * current, low, middle, position, new_value)
        else:
            self._modify_tree(2 * current + 1, middle + 1, high, position, new_value)
        self.segment[current] = self.segment[2 * current] + self.segment[2 * current + 1]

    def sumRange(self, left_end, right_end):
        return self._range_query(1, 0, self.length - 1, left_end, right_end)

    def _range_query(self, current, low, high, left_end, right_end):
        if right_end < low or high < left_end:
            return 0
        if left_end <= low and high <= right_end:
            return self.segment[current]
        middle = (low + high) // 2
        left_sum = self._range_query(2 * current, low, middle, left_end, right_end)
        right_sum = self._range_query(2 * current + 1, middle + 1, high, left_end, right_end)
        return left_sum + right_sum
