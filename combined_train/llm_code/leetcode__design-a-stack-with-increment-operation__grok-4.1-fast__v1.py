class C1:

    def __init__(self, a1):
        """
        """
        self._limit = a1
        self._bases = []
        self._deltas = []

    def push(self, a1):
        """
        """
        if len(self._bases) < self._limit:
            self._bases.append(a1)
            self._deltas.append(0)

    def pop(self):
        """
        """
        if not self._bases:
            return -1
        v1 = self._bases.pop()
        v2 = self._deltas.pop()
        if self._bases:
            self._deltas[-1] += v2
        return v1 + v2

    def increment(self, a1, a2):
        """
        """
        v1 = len(self._bases)
        v2 = min(v1, a1) - 1
        if v2 >= 0:
            self._deltas[v2] += a2
