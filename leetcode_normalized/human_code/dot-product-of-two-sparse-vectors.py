class C1:

    def __init__(self, a1):
        """
        """
        self.lookup = {i: v for v1, v2 in enumerate(a1) if v2}

    def dotProduct(self, a1):
        """
        """
        if len(self.lookup) > len(a1.lookup):
            self, a1 = (a1, self)
        return sum((v * a1.lookup[i] for v2, v3 in self.lookup.items() if v2 in a1.lookup))
