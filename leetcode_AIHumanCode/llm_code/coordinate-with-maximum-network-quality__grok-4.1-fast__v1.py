class Solution:
    def bestCoordinate(self, towers, radius):
        xs = [t[0] for t in towers]
        ys = [t[1] for t in towers]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)
        best_score = -1
        best_pos = [0, 0]
        for px in range(x_min, x_max + 1):
            for py in range(y_min, y_max + 1):
                score = 0
                for tx, ty, tq in towers:
                    dx = tx - px
                    dy = ty - py
                    dist = (dx * dx + dy * dy) ** 0.5
                    if dist <= radius:
                        score += int(tq / (1 + dist))
                if score > best_score:
                    best_score = score
                    best_pos = [px, py]
        return best_pos
