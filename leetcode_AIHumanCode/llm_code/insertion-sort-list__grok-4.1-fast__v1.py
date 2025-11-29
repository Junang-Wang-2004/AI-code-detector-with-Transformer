class Solution:
    def insertionSortList(self, head):
        sentinel = ListNode(0)
        sentinel.next = None
        node = head
        while node:
            succ = node.next
            spot = sentinel
            while spot.next and spot.next.val <= node.val:
                spot = spot.next
            node.next = spot.next
            spot.next = node
            node = succ
        return sentinel.next
