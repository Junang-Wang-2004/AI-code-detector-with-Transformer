class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)

    def modify(self, index, value):
        while index <= self.size:
            self.data[index] += value
            index += index & -index

    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.data[index]
            index -= index & -index
        return total


class Solution:
    def processQueries(self, queries, m):
        tree = FenwickTree(2 * m + 1)
        pos_of = [0] * (m + 1)
        next_front = m
        answers = []
        for num in range(1, m + 1):
            spot = m + num
            pos_of[num] = spot
            tree.modify(spot, 1)
        for query in queries:
            current_spot = pos_of[query]
            answers.append(tree.prefix_sum(current_spot - 1))
            tree.modify(current_spot, -1)
            pos_of[query] = next_front
            tree.modify(next_front, 1)
            next_front -= 1
        return answers
