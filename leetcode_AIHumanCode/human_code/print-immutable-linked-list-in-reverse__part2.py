# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def printLinkedListInReverse(self, head):
        """
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.getNext()
        for node in reversed(nodes):
            node.printValue()


