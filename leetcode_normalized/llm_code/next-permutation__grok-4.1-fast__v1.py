class C1(object):

    def nextPermutation(self, a1):
        v1 = len(a1)
        v2 = v1 - 2
        while v2 >= 0 and a1[v2] >= a1[v2 + 1]:
            v2 -= 1
        if v2 < 0:
            self.reverse_range(a1, 0, v1 - 1)
            return
        v3 = v1 - 1
        while v3 > v2 and a1[v3] <= a1[v2]:
            v3 -= 1
        a1[v2], a1[v3] = (a1[v3], a1[v2])
        self.reverse_range(a1, v2 + 1, v1 - 1)

    def reverse_range(self, a1, a2, a3):
        while a2 < a3:
            a1[a2], a1[a3] = (a1[a3], a1[a2])
            a2 += 1
            a3 -= 1
