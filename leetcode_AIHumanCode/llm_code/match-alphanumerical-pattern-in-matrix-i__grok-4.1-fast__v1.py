class Solution(object):
    def findPattern(self, board, pattern):
        if not pattern or not board:
            return [-1, -1]
        
        br, bc = len(board), len(board[0])
        pr, pc = len(pattern), len(pattern[0])
        
        def matches(sr, sc):
            assign = {}
            taken = set()
            for dr in range(pr):
                for dc in range(pc):
                    cell = board[sr + dr][sc + dc]
                    sym = pattern[dr][dc]
                    if sym.isdigit():
                        if int(sym) != cell:
                            return False
                    else:
                        if sym not in assign:
                            if cell in taken:
                                return False
                            taken.add(cell)
                            assign[sym] = cell
                        elif assign[sym] != cell:
                            return False
            return True
        
        for sr in range(br - pr + 1):
            for sc in range(bc - pc + 1):
                if matches(sr, sc):
                    return [sr, sc]
        return [-1, -1]
