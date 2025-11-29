class C1(object):

    def kthSmallest(self, a1, a2):
        v1, v2, v3 = ([], a1, 0)
        while v1 or v2:
            if v2:
                v1.append(v2)
                v2 = v2.left
            else:
                v2 = v1.pop()
                v3 += 1
                if v3 == a2:
                    return v2.val
                v2 = v2.right
        return float('-inf')
from itertools import islice
