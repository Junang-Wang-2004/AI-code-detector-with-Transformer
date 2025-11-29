"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class C1(object):

    def findSolution(self, a1, a2):
        """
        """
        v1 = []
        v2, v3 = (1, 1)
        while a1.f(v2, v3) < a2:
            v3 += 1
        while v3 > 0:
            while v3 > 0 and a1.f(v2, v3) > a2:
                v3 -= 1
            if v3 > 0 and a1.f(v2, v3) == a2:
                v1.append([v2, v3])
            v2 += 1
        return v1
