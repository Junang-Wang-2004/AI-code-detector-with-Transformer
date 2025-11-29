from collections import defaultdict, deque

class C1:

    def findClosestLeaf(self, a1, a2):
        v1 = defaultdict(list)
        v2 = set()
        v3 = deque([a1])
        while v3:
            v4 = v3.popleft()
            if not v4.left and (not v4.right):
                v2.add(v4.val)
            if v4.left:
                v1[v4.val].append(v4.left.val)
                v1[v4.left.val].append(v4.val)
                v3.append(v4.left)
            if v4.right:
                v1[v4.val].append(v4.right.val)
                v1[v4.right.val].append(v4.val)
                v3.append(v4.right)
        v5 = deque([a2])
        v6 = set([a2])
        while v5:
            v7 = v5.popleft()
            if v7 in v2:
                return v7
            for v8 in v1[v7]:
                if v8 not in v6:
                    v6.add(v8)
                    v5.append(v8)
        return 0
