class C1:

    def confusingNumber(self, a1):
        v1 = str(a1)
        v2 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        v3 = set(v2)
        if not all((c in v3 for v4 in v1)):
            return False
        v5 = ''.join((v2[v4] for v4 in reversed(v1)))
        return v5 != v1
