from collections import Counter, defaultdict, deque

class FreqStack:
    def __init__(self):
        self.frequencies = Counter()
        self.stacks = defaultdict(deque)
        self.highest = 0

    def push(self, val):
        curr_freq = self.frequencies[val]
        new_freq = curr_freq + 1
        self.frequencies[val] = new_freq
        self.stacks[new_freq].append(val)
        if new_freq > self.highest:
            self.highest = new_freq

    def pop(self):
        item = self.stacks[self.highest].pop()
        self.frequencies[item] -= 1
        if self.frequencies[item] == 0:
            del self.frequencies[item]
        if not self.stacks[self.highest]:
            del self.stacks[self.highest]
            self.highest -= 1
        return item
