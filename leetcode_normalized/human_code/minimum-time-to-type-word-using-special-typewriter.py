class C1(object):

    def minTimeToType(self, a1):
        """
        """
        return min((ord(a1[0]) - ord('a')) % 26, (ord('a') - ord(a1[0])) % 26) + 1 + sum((min((ord(a1[i]) - ord(a1[i - 1])) % 26, (ord(a1[i - 1]) - ord(a1[i])) % 26) + 1 for v1 in range(1, len(a1))))
