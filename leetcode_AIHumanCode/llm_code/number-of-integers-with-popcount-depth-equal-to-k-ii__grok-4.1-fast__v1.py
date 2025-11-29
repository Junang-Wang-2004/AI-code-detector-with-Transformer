class Solution(object):
    def popcountDepth(self, nums, queries):
        def pop_cnt(num):
            return bin(num).count('1')

        def get_depth(val):
            steps = 0
            current = val
            while True:
                if current == 1:
                    return steps
                if current == 0:
                    return steps + 1
                current = pop_cnt(current)
                steps += 1

        length = len(nums)
        max_k = 0
        current_max = 10**15
        while current_max != 1:
            current_max = (current_max - 1).bit_length()
            max_k += 1

        class FenwickTree(object):
            def __init__(self, capacity):
                self.capacity = capacity
                self.tree_arr = [0] * (capacity + 1)

            def update(self, pos, delta):
                pos += 1
                while pos <= self.capacity:
                    self.tree_arr[pos] += delta
                    pos += pos & -pos

            def prefix_sum(self, pos):
                pos += 1
                accum = 0
                while pos > 0:
                    accum += self.tree_arr[pos]
                    pos -= pos & -pos
                return accum

        fenwicks = [FenwickTree(length) for _ in range(max_k + 1)]

        for idx in range(length):
            dep = get_depth(nums[idx])
            fenwicks[dep].update(idx, 1)

        answers = []
        for instruction in queries:
            if instruction[0] == 1:
                start = instruction[1]
                end = instruction[2]
                target_k = instruction[3]
                count = fenwicks[target_k].prefix_sum(end) - fenwicks[target_k].prefix_sum(start - 1)
                answers.append(count)
            else:
                idx = instruction[1]
                updated_val = instruction[2]
                prior_val = nums[idx]
                prior_dep = get_depth(prior_val)
                updated_dep = get_depth(updated_val)
                nums[idx] = updated_val
                if prior_dep != updated_dep:
                    fenwicks[prior_dep].update(idx, -1)
                    fenwicks[updated_dep].update(idx, 1)
        return answers
