MOD = 10**9 + 7

class FenwickTree:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * (capacity + 2)

    def modify(self, index, amount):
        index += 1
        while index <= self.capacity:
            self.data[index] = (self.data[index] + amount) % MOD
            index += index & -index

    def accumulate(self, index):
        index += 1
        total = 0
        while index > 0:
            total = (total + self.data[index]) % MOD
            index -= index & -index
        return total


class Solution:
    def totalBeauty(self, nums):
        if not nums:
            return 0
        max_val = max(nums)
        containers = [[] for _ in range(max_val + 1)]
        for num in nums:
            divisors = []
            divisor = 1
            while divisor * divisor <= num:
                if num % divisor == 0:
                    divisors.append(divisor)
                    if divisor != num // divisor:
                        divisors.append(num // divisor)
                divisor += 1
            for div in divisors:
                containers[div].append(num)

        totients = list(range(max_val + 1))
        for p in range(2, max_val + 1):
            if totients[p] == p:
                for multiple in range(p, max_val + 1, p):
                    totients[multiple] = (totients[multiple] // p) * (p - 1)

        result = 0
        for divisor in range(1, max_val + 1):
            sequence = containers[divisor]
            if not sequence:
                continue
            unique_sorted = sorted(set(sequence))
            position_map = {value: pos for pos, value in enumerate(unique_sorted)}
            tree_size = len(unique_sorted)
            tree = FenwickTree(tree_size)
            for value in sequence:
                pos = position_map[value]
                prior_sum = tree.accumulate(pos - 1) if pos > 0 else 0
                increment = (prior_sum + 1) % MOD
                tree.modify(pos, increment)
            subseq_count = tree.accumulate(tree_size - 1)
            result = (result + totients[divisor] * subseq_count) % MOD
        return result
