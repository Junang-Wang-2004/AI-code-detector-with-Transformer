class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        node_map = {}
        iter_node = head
        while iter_node:
            node_map[iter_node] = Node(iter_node.val)
            iter_node = iter_node.next
        
        copy_root = node_map[head]
        iter_node = head
        while iter_node:
            copy_node = node_map[iter_node]
            copy_node.next = node_map.get(iter_node.next, None)
            copy_node.random = node_map.get(iter_node.random, None)
            iter_node = iter_node.next
        
        return copy_root
