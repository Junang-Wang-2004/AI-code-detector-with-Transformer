class CustomStack:

    def __init__(self, maximum):
        """
        """
        self._limit = maximum
        self._bases = []
        self._deltas = []

    def push(self, number):
        """
        """
        if len(self._bases) < self._limit:
            self._bases.append(number)
            self._deltas.append(0)

    def pop(self):
        """
        """
        if not self._bases:
            return -1
        base = self._bases.pop()
        delta = self._deltas.pop()
        if self._bases:
            self._deltas[-1] += delta
        return base + delta

    def increment(self, count, value):
        """
        """
        size = len(self._bases)
        pos = min(size, count) - 1
        if pos >= 0:
            self._deltas[pos] += value
