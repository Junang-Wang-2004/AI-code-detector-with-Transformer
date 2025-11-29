class C1(object):

    def triangleType(self, a1):
        """
        """
        a1.sort()
        v1, v2, v3 = a1
        if v1 + v2 <= v3:
            return 'none'
        if v1 == v2 == v3:
            return 'equilateral'
        if v1 == v2 or v2 == v3:
            return 'isosceles'
        return 'scalene'
