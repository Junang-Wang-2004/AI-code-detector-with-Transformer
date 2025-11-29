class Solution(object):
    def rotateTheBox(self, box):
        return [list(row) for row in zip(*box[::-1])]
