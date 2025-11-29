import random

class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def kthLargestLevelSum(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3=0, a4=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1 = len(a1) - 1
            while a3 <= v1:
                v2 = random.randint(a3, v1)
                v3, v4 = tri_partition(a1, a3, v1, a1[v2], a4)
                if v3 <= a2 <= v4:
                    return
                elif v3 > a2:
                    v1 = v3 - 1
                else:
                    a3 = v4 + 1
        v1 = []
        v2 = [a1]
        while v2:
            v3 = []
            for v4 in v2:
                if v4.left:
                    v3.append(v4.left)
                if v4.right:
                    v3.append(v4.right)
            v1.append(sum((x.val for v5 in v2)))
            v2 = v3
        if a2 - 1 >= len(v1):
            return -1
        nth_element(v1, a2 - 1, compare=lambda a, b: a > b)
        return v1[a2 - 1]
