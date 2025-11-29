import bisect

class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def countGreatEnoughNodes(self, a1, a2):
        """
        """

        def merge_at_most_k(a1, a2):
            v1 = []
            v2 = v3 = 0
            while v2 < len(a1) or v3 < len(a2):
                if v3 == len(a2) or (v2 < len(a1) and a1[v2] < a2[v3]):
                    v1.append(a1[v2])
                    v2 += 1
                else:
                    v1.append(a2[v3])
                    v3 += 1
                if len(v1) == a2:
                    break
            return v1

        def merge_sort(a1):
            if not a1:
                return []
            v1, v2 = (merge_sort(a1.left), merge_sort(a1.right))
            v3 = merge_at_most_k(v1, v2)
            v4 = bisect.bisect_left(v3, a1.val)
            if v4 == a2:
                result[0] += 1
            else:
                v3.insert(v4, a1.val)
                if len(v3) == a2 + 1:
                    v3.pop()
            return v3
        v1 = [0]
        merge_sort(a1)
        return v1[0]
