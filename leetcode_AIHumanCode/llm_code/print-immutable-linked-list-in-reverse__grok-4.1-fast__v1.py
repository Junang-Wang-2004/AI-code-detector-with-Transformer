class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        """
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.getNext()
        while stack:
            stack.pop().printValue()
