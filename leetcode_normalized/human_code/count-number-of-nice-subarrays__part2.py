import collections

class C1(object):

    def numberOfSubarrays(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.deque([-1])
        for v3 in range(len(a1)):
            if a1[v3] % 2:
                v2.append(v3)
            if len(v2) > a2 + 1:
                v2.popleft()
            if len(v2) == a2 + 1:
                v1 += v2[1] - v2[0]
        return v1
