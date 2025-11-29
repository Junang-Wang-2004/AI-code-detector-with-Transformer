class C1:

    def categorizeBox(self, a1, a2, a3, a4):
        v1 = max(a1, a2, a3)
        v2 = a1 * a2 * a3
        v3 = v1 >= 10000 or v2 >= 1000000000
        v4 = a4 >= 100
        if v3:
            return ['Bulky', 'Both'][v4]
        return ['Neither', 'Heavy'][v4]
