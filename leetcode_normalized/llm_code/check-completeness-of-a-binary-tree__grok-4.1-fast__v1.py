from collections import deque

class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def isCompleteTree(self, a1):
        v1 = deque([a1])
        v2 = False
        while v1:
            v3 = v1.popleft()
            if v2 and v3:
                return False
            if v3:
                v1.append(v3.left)
                v1.append(v3.right)
            else:
                v2 = True
        return True
