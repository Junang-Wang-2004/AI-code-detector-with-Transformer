class C1:

    def maxKDistinct(self, a1, a2):
        v1 = list(set(a1))
        v1.sort(reverse=True)
        return v1[:a2]
