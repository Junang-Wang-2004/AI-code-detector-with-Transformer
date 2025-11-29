from collections import deque

class C1(object):

    def connect(self, a1):
        if not a1:
            return
        v1 = deque([a1])
        while v1:
            v2 = len(v1)
            v3 = None
            for v4 in range(v2):
                v5 = v1.popleft()
                if v3:
                    v3.next = v5
                v3 = v5
                if v5.left:
                    v1.append(v5.left)
                if v5.right:
                    v1.append(v5.right)
