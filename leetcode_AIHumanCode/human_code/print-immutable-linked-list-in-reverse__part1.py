# Time:  O(n)
# Space: O(sqrt(n))

import math


class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        """
        def print_nodes(head, count):
            nodes = []
            while head and len(nodes) != count:
                nodes.append(head)
                head = head.getNext()
            for node in reversed(nodes):
                node.printValue()
                   
        count = 0
        curr = head
        while curr:
            curr = curr.getNext()
            count += 1
        bucket_count = int(math.ceil(count**0.5))
        
        buckets = []
        count = 0
        curr = head
        while curr:
            if count % bucket_count == 0:
                buckets.append(curr)
            curr = curr.getNext()
            count += 1
        for node in reversed(buckets):
            print_nodes(node, bucket_count)
            
        
