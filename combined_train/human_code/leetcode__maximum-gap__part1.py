class C1(object):

    def maximumGap(self, a1):
        """
        """
        if len(a1) < 2:
            return 0
        v1, v2 = (max(a1), min(a1))
        v3 = max(1, (v1 - v2) / (len(a1) - 1))
        v4 = (v1 - v2) / v3 + 1
        v5 = [{'min': float('inf'), 'max': float('-inf')} for v6 in range(v4)]
        for v7 in a1:
            if v7 in (v1, v2):
                continue
            v8 = (v7 - v2) / v3
            v5[v8]['min'] = min(v5[v8]['min'], v7)
            v5[v8]['max'] = max(v5[v8]['max'], v7)
        v9, v10 = (0, v2)
        for v8 in range(v4):
            if v5[v8]['min'] == float('inf') and v5[v8]['max'] == float('-inf'):
                continue
            v9 = max(v9, v5[v8]['min'] - v10)
            v10 = v5[v8]['max']
        v9 = max(v9, v1 - v10)
        return v9
