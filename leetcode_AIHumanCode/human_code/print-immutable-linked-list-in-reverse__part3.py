# Time:  O(n^2)
# Space: O(1)
class Solution3(object):
    def printLinkedListInReverse(self, head):
        """
        """
        tail = None
        while head != tail:
            curr = head
            while curr.getNext() != tail:
                curr = curr.getNext()
            curr.printValue()
            tail = curr
