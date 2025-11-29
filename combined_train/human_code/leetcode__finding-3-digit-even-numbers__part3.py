import collections

class C1(object):

    def __init__(self, a1=None, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def findEvenNumbers(self, a1):
        """
        """
        v1 = 3

        def backtracking(a1, a2, a3):
            if len(a1) == v1:
                a3.append(reduce(lambda x, y: x * 10 + y, a1))
                return
            v1 = a2.right
            while v1:
                if not a1 and v1.val[0] == 0 or (len(a1) == v1 - 1 and v1.val[0] % 2 != 0):
                    v1 = v1.right
                    continue
                v1.val[1] -= 1
                if v1.val[1] == 0:
                    if v1.left:
                        v1.left.right = v1.right
                    if v1.right:
                        v1.right.left = v1.left
                a1.append(v1.val[0])
                backtracking(a1, a2, a3)
                a1.pop()
                if v1.val[1] == 0:
                    if v1.left:
                        v1.left.right = v1
                    if v1.right:
                        v1.right.left = v1
                v1.val[1] += 1
                v1 = v1.right
        v2 = v3 = C1()
        for v4, v5 in sorted(map(list, iter(collections.Counter(a1).items()))):
            v2.right = C1(val=[v4, v5], left=v2)
            v2 = v2.right
        v6 = []
        backtracking([], v3, v6)
        return v6
