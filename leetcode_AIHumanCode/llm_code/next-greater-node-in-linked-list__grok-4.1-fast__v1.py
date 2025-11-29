class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head):
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        n = len(values)
        output = [0] * n
        monotonic = []
        for idx in range(n - 1, -1, -1):
            while monotonic and monotonic[-1] <= values[idx]:
                monotonic.pop()
            if monotonic:
                output[idx] = monotonic[-1]
            monotonic.append(values[idx])
        return output
