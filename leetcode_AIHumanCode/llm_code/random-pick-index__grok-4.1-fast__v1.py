import random
import collections

class Solution:
    def __init__(self, numbers):
        self.index_map = collections.defaultdict(list)
        for position in range(len(numbers)):
            value = numbers[position]
            self.index_map[value].append(position)

    def pick(self, value):
        positions = self.index_map[value]
        return positions[random.randrange(len(positions))]
