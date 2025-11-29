class Solution:
    def modifiedList(self, nums, head):
        banned = set(nums)
        prev_node = None
        current = head
        while current:
            if current.val in banned:
                if prev_node is None:
                    head = current.next
                else:
                    prev_node.next = current.next
            else:
                prev_node = current
            current = current.next
        return head
