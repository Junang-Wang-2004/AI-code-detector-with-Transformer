class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        output = []
        pile = [(root, 0)]
        while pile:
            current, pointer = pile[-1]
            if pointer == 0:
                output.append(current.val)
            if pointer < len(current.children):
                next_child = current.children[pointer]
                pile[-1] = (current, pointer + 1)
                if next_child:
                    pile.append((next_child, 0))
            else:
                pile.pop()
        return output
