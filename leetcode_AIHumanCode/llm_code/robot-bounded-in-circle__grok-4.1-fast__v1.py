class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        px, py = 0, 0
        face = 0
        delta_x = [0, 1, 0, -1]
        delta_y = [1, 0, -1, 0]
        for cmd in instructions:
            if cmd == 'G':
                px += delta_x[face]
                py += delta_y[face]
            elif cmd == 'R':
                face = (face + 1) % 4
            else:
                face = (face + 3) % 4
        return px == 0 and py == 0 or face != 0
