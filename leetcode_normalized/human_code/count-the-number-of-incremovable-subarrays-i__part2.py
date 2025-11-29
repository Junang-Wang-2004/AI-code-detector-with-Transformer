class C1(object):

    def incremovableSubarrayCount(self, a1):
        """
        """
        return sum(((left == 0 or right == len(a1) - 1 or a1[left - 1] < a1[right + 1]) and all((a1[i] < a1[i + 1] for v1 in range(left - 1))) and all((a1[v1] < a1[v1 + 1] for v1 in range(right + 1, len(a1) - 1))) for v2 in range(len(a1)) for v3 in range(v2, len(a1))))
