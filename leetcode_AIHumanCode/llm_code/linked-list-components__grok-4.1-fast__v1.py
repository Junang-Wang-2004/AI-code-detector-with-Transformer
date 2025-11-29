class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        target_values = set(G)
        components = 0
        current = head
        previous_included = False
        while current:
            included = current.val in target_values
            if included and not previous_included:
                components += 1
            previous_included = included
            current = current.next
        return components
