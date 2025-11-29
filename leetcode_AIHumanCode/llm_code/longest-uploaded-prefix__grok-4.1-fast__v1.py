class LUPrefix:

    def __init__(self, n):
        self.seen = [False] * (n + 1)
        self.max_prefix = 0

    def upload(self, video):
        self.seen[video] = True
        while self.max_prefix < n and self.seen[self.max_prefix + 1]:
            self.max_prefix += 1

    def longest(self):
        return self.max_prefix
