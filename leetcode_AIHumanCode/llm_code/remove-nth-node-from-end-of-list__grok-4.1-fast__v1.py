class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        sentinel = ListNode(0)
        sentinel.next = head
        leader = sentinel
        for _ in range(n + 1):
            leader = leader.next
        follower = sentinel
        while leader:
            follower = follower.next
            leader = leader.next
        follower.next = follower.next.next
        return sentinel.next
