class C1(object):

    def smallestNumber(self, a1):
        """
        """
        v1 = 1 if a1 >= 0 else -1
        v2 = sorted(str(abs(a1)), reverse=v1 == -1)
        v3 = next((v3 for v3 in range(len(v2)) if v2[v3] != '0'), 0)
        v2[0], v2[v3] = (v2[v3], v2[0])
        return v1 * int(''.join(v2))
