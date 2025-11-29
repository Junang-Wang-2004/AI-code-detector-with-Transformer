class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        class Node:
            def __init__(self, val):
                self.val = val
                self.prev = None
                self.next = None

        if n == 0:
            return [0] * len(queries)

        nodes = [Node(i) for i in range(n)]
        for i in range(n):
            if i > 0:
                nodes[i].prev = nodes[i - 1]
            if i < n - 1:
                nodes[i].next = nodes[i + 1]

        val_to_node = {i: nodes[i] for i in range(n)}
        remaining = n
        ans = []

        for start, end in queries:
            if start >= end:
                ans.append(remaining - 1)
                continue
            left_node = val_to_node[start]
            right_node = val_to_node[end]
            walker = left_node.next
            while walker != right_node:
                nxt = walker.next
                walker.prev.next = walker.next
                walker.next.prev = walker.prev
                del val_to_node[walker.val]
                remaining -= 1
                walker = nxt
            ans.append(remaining - 1)

        return ans
