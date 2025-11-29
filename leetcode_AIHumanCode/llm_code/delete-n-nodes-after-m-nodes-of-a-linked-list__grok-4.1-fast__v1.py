# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteNodes(self, head, m, n):
        sentinel = ListNode(next=head)
        runner = sentinel
        while runner.next:
            kept = 0
            while kept < m and runner.next:
                runner = runner.next
                kept += 1
            to_connect = runner.next
            skipped = 0
            while skipped < n and to_connect:
                to_connect = to_connect.next
                skipped += 1
            runner.next = to_connect
        return sentinel.next
