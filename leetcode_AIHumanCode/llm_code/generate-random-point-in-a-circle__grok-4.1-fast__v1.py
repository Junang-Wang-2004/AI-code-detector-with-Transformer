import random
import math

class Solution:
    def __init__(self, radius, x_center, y_center):
        self.cx = x_center
        self.cy = y_center
        self.rsq = radius * radius

    def randPoint(self):
        while True:
            dx = random.uniform(-math.sqrt(self.rsq), math.sqrt(self.rsq))
            dy = random.uniform(-math.sqrt(self.rsq), math.sqrt(self.rsq))
            if dx * dx + dy * dy <= self.rsq:
                return self.cx + dx, self.cy + dy
