import random

class C1(object):

    def kthLargestPerfectSubtree(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3, a4, a5=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4):
                v1 = a2
                while v1 <= a3:
                    if a5(a1[v1], a4):
                        a1[v1], a1[a2] = (a1[a2], a1[v1])
                        a2 += 1
                        v1 += 1
                    elif a5(a4, a1[v1]):
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                    else:
                        v1 += 1
                return (a2, a3)
            while a2 <= a4:
                v1 = random.randint(a2, a4)
                v2, v3 = tri_partition(a1, a2, a4, a1[v1])
                if v2 <= a3 <= v3:
                    return
                elif v2 > a3:
                    a4 = v2 - 1
                else:
                    a2 = v3 + 1

        def dfs(a1):
            if not a1:
                result.append(0)
                return
            dfs(a1.left)
            v1 = result[-1]
            dfs(a1.right)
            v2 = result[-1]
            result.append(v1 + v2 + 1 if v1 == v2 != -1 else -1)
        v1 = []
        dfs(a1)
        nth_element(v1, 0, a2 - 1, len(v1) - 1, lambda a, b: a > b)
        return v1[a2 - 1] if a2 - 1 < len(v1) and v1[a2 - 1] > 0 else -1
