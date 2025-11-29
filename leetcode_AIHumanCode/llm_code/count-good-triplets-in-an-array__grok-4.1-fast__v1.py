class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)

    def update(self, index, delta):
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        position = [0] * n
        for idx, val in enumerate(nums1):
            position[val] = idx

        right_greater = [0] * n
        ft_right = FenwickTree(n)
        for idx in range(n - 1, -1, -1):
            pos_val = position[nums2[idx]]
            right_greater[idx] = ft_right.query(n - 1) - ft_right.query(pos_val)
            ft_right.update(pos_val, 1)

        total = 0
        ft_left = FenwickTree(n)
        for idx in range(n):
            pos_val = position[nums2[idx]]
            left_smaller = ft_left.query(pos_val - 1)
            total += left_smaller * right_greater[idx]
            ft_left.update(pos_val, 1)

        return total
