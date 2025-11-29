from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.point_count = defaultdict(lambda: defaultdict(int))

    def add(self, coord):
        cx, cy = coord
        self.point_count[cx][cy] += 1

    def count(self, coord):
        px, py = coord
        ans = 0
        neighbors_y = list(self.point_count[px])
        for ny in neighbors_y:
            if ny == py:
                continue
            side = abs(ny - py)
            ans += (self.point_count[px][ny] *
                    self.point_count[px + side][py] *
                    self.point_count[px + side][ny])
            ans += (self.point_count[px][ny] *
                    self.point_count[px - side][py] *
                    self.point_count[px - side][ny])
        return ans
