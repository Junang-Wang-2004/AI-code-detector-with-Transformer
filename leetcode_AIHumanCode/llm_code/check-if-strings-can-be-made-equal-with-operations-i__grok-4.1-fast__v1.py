class Solution:
    def canBeEqual(self, str_a, str_b):
        pair1_a = sorted(str_a[0] + str_a[2])
        pair1_b = sorted(str_b[0] + str_b[2])
        pair2_a = sorted(str_a[1] + str_a[3])
        pair2_b = sorted(str_b[1] + str_b[3])
        return pair1_a == pair1_b and pair2_a == pair2_b
