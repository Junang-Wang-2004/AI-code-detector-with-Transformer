class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        lx1, rx1, by1, ty1 = A, C, B, D
        lx2, rx2, by2, ty2 = E, G, F, H
        rect1_area = (rx1 - lx1) * (ty1 - by1)
        rect2_area = (rx2 - lx2) * (ty2 - by2)
        oxl = max(lx1, lx2)
        oxr = min(rx1, rx2)
        oyb = max(by1, by2)
        oyt = min(ty1, ty2)
        inter_w = max(0, oxr - oxl)
        inter_h = max(0, oyt - oyb)
        return rect1_area + rect2_area - inter_w * inter_h
