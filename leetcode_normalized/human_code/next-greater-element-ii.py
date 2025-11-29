class C1(object):

    def nextGreaterElements(self, a1):
        """
        """
        v1, v2 = ([0] * len(a1), [])
        for v3 in reversed(range(2 * len(a1))):
            while v2 and v2[-1] <= a1[v3 % len(a1)]:
                v2.pop()
            v1[v3 % len(a1)] = v2[-1] if v2 else -1
            v2.append(a1[v3 % len(a1)])
        return v1
