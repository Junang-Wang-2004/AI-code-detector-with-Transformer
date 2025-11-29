from collections import defaultdict, deque

class Solution:
    def findClosestLeaf(self, root, k):
        adj = defaultdict(list)
        leaf_set = set()
        traversal = deque([root])
        while traversal:
            current = traversal.popleft()
            if not current.left and not current.right:
                leaf_set.add(current.val)
            if current.left:
                adj[current.val].append(current.left.val)
                adj[current.left.val].append(current.val)
                traversal.append(current.left)
            if current.right:
                adj[current.val].append(current.right.val)
                adj[current.right.val].append(current.val)
                traversal.append(current.right)
        search = deque([k])
        visited = set([k])
        while search:
            node = search.popleft()
            if node in leaf_set:
                return node
            for adjacent in adj[node]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    search.append(adjacent)
        return 0
