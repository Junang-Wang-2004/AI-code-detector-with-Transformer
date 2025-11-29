class C1(object):

    def confusingNumber(self, a1):
        """
        """
        v1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        v2 = str(a1)
        v3 = []
        for v4 in range(len(v2)):
            if v2[v4] not in v1:
                return False
        for v4 in range((len(v2) + 1) // 2):
            if v2[v4] != v1[v2[-(v4 + 1)]]:
                return True
        return False
