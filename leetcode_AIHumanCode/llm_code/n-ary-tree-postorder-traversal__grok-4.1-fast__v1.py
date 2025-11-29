class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        output = []
        pile = [(root, 0)]
        while pile:
            current, pointer = pile[-1]
            if pointer < len(current.children):
                pile[-1] = (current, pointer + 1)
                nxt = current.children[pointer]
                if nxt:
                    pile.append((nxt, 0))
            else:
                output.append(current.val)
                pile.pop()
        return output
