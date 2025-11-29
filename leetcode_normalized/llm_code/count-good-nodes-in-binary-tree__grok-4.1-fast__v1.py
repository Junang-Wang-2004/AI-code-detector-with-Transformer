from collections import deque

class C1(object):

    def goodNodes(self, a1):
        if not a1:
            return 0
        v1 = deque([(a1, a1.val)])
        v2 = 0
        while v1:
            v3, v4 = v1.popleft()
            if v3.val >= v4:
                v2 += 1
            v5 = max(v4, v3.val)
            if v3.left:
                v1.append((v3.left, v5))
            if v3.right:
                v1.append((v3.right, v5))
        return v2
