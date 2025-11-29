class C1(object):

    def findMinFibonacciNumbers(self, a1):
        v1 = [1, 1]
        while v1[-1] + v1[-2] <= a1:
            v1.append(v1[-1] + v1[-2])
        v2 = 0
        for v3 in v1[::-1]:
            while a1 >= v3:
                a1 -= v3
                v2 += 1
        return v2
