class C1(object):

    def smallestPalindrome(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in range(len(a1) // 2):
            v1[ord(a1[v2]) - ord('a')] += 1
        v3 = [chr(ord('a') + v2) * c for v2, v4 in enumerate(v1)]
        if len(a1) % 2:
            v3.append(a1[len(a1) // 2])
        v3.extend((v3[v2] for v2 in reversed(range(len(v3) - len(a1) % 2))))
        return ''.join(v3)
