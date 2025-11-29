class C1:

    def __init__(self, a1):
        self.seen = [False] * (a1 + 1)
        self.max_prefix = 0

    def upload(self, a1):
        self.seen[a1] = True
        while self.max_prefix < n and self.seen[self.max_prefix + 1]:
            self.max_prefix += 1

    def longest(self):
        return self.max_prefix
