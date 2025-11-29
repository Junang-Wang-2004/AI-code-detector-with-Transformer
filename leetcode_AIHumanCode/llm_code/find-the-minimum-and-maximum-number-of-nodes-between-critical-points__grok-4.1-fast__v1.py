class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        criticals = []
        position = 1
        current = head
        while current.next and current.next.next:
            if (current.next.val > current.val and current.next.val > current.next.next.val) or \
               (current.next.val < current.val and current.next.val < current.next.next.val):
                criticals.append(position + 1)
            position += 1
            current = current.next
        if len(criticals) < 2:
            return [-1, -1]
        min_gap = min(criticals[j + 1] - criticals[j] for j in range(len(criticals) - 1))
        return [min_gap, criticals[-1] - criticals[0]]
