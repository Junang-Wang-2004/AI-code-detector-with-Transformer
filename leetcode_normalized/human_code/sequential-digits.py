import collections

class C1(object):

    def sequentialDigits(self, a1, a2):
        """
        """
        v1 = []
        v2 = collections.deque(list(range(1, 9)))
        while v2:
            v3 = v2.popleft()
            if v3 > a2:
                continue
            if a1 <= v3:
                v1.append(v3)
            if v3 % 10 + 1 < 10:
                v2.append(v3 * 10 + v3 % 10 + 1)
        return v1
