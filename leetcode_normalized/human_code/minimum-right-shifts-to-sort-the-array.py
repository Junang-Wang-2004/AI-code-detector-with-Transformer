class C1(object):

    def minimumRightShifts(self, a1):
        """
        """
        v1 = next((v1 for v1 in range(len(a1)) if not a1[v1] < a1[(v1 + 1) % len(a1)]), len(a1))
        v2 = next((v2 for v2 in range(v1 + 1, len(a1)) if not a1[v2 % len(a1)] < a1[(v2 + 1) % len(a1)]), len(a1))
        return len(a1) - (v1 + 1) if v2 == len(a1) else -1
