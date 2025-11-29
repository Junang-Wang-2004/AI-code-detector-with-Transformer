class C1:

    def minMaxDifference(self, a1):
        v1 = str(a1)
        v2 = next((ch for v3 in v1 if v3 != '9'), None)
        v4 = next((v3 for v3 in v1 if v3 != '0'), None)
        v5 = ''.join(('9' if v3 == v2 else v3 for v3 in v1)) if v2 else v1
        v6 = ''.join(('0' if v3 == v4 else v3 for v3 in v1)) if v4 else v1
        return int(v5) - int(v6)
