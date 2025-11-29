import bisect

class CountIntervals:
    def __init__(self):
        self.data = []
        self.total = 0

    def add(self, left, right):
        i = bisect.bisect_left(self.data, (left,))
        if i > 0 and self.data[i - 1][1] >= left - 1:
            i -= 1
            left = self.data[i][0]
        new_right = right
        j = i
        while j < len(self.data) and self.data[j][0] <= new_right + 1:
            new_right = max(new_right, self.data[j][1])
            self.total -= self.data[j][1] - self.data[j][0] + 1
            j += 1
        del self.data[i:j]
        self.data.insert(i, (left, new_right))
        self.total += new_right - left + 1

    def count(self):
        return self.total
