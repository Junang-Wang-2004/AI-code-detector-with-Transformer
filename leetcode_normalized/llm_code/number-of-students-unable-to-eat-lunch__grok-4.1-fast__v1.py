class C1:

    def countStudents(self, a1, a2):
        v1 = [a1.count(0), a1.count(1)]
        v2 = 0
        v3 = len(a2)
        while v2 < v3 and v1[a2[v2]] > 0:
            v1[a2[v2]] -= 1
            v2 += 1
        return v3 - v2
