class Solution:
    def resultGrid(self, image, threshold):
        h, w = len(image), len(image[0])
        accum = [[0] * w for _ in range(h)]
        covers = [[0] * w for _ in range(h)]
        for ci in range(1, h - 1):
            for cj in range(1, w - 1):
                good = True
                # vertical diffs
                for x in range(3):
                    for y in range(2):
                        r1, r2 = ci - 1 + y, ci - 1 + y + 1
                        if abs(image[r1][cj - 1 + x] - image[r2][cj - 1 + x]) > threshold:
                            good = False
                            break
                    if not good:
                        break
                if not good:
                    continue
                # horizontal diffs
                for y in range(3):
                    for x in range(2):
                        c1, c2 = cj - 1 + x, cj - 1 + x + 1
                        if abs(image[ci - 1 + y][c1] - image[ci - 1 + y][c2]) > threshold:
                            good = False
                            break
                    if not good:
                        break
                if not good:
                    continue
                # compute average
                s = sum(image[ci - 1 + dy][cj - 1 + dx] for dy in range(3) for dx in range(3))
                avg = s // 9
                # vote
                for dy in range(3):
                    for dx in range(3):
                        ri, rj = ci - 1 + dy, cj - 1 + dx
                        accum[ri][rj] += avg
                        covers[ri][rj] += 1
        # finalize
        for i in range(h):
            for j in range(w):
                if covers[i][j] > 0:
                    accum[i][j] //= covers[i][j]
                else:
                    accum[i][j] = image[i][j]
        return accum
