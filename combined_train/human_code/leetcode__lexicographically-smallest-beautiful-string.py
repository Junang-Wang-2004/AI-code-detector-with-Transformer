class C1(object):

    def smallestBeautifulString(self, a1, a2):
        """
        """

        def check(a1):
            return (a1 - 1 < 0 or arr[a1 - 1] != arr[a1]) and (a1 - 2 < 0 or arr[a1 - 2] != arr[a1])
        v1 = [ord(x) - ord('a') for v2 in a1]
        for v3 in reversed(range(len(v1))):
            v1[v3] += 1
            while not check(v3):
                v1[v3] += 1
            if v1[v3] < a2:
                break
        else:
            return ''
        for v4 in range(v3 + 1, len(v1)):
            v1[v4] = 0
            while not check(v4):
                v1[v4] += 1
        return ''.join([chr(ord('a') + v2) for v2 in v1])
