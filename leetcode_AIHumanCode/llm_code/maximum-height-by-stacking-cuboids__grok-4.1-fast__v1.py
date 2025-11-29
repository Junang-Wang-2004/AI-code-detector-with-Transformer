class Solution(object):
    def maxHeight(self, cuboids):
        sorted_boxes = [sorted(box) for box in cuboids]
        sorted_boxes.append([0] * 3)
        sorted_boxes.sort()
        n = len(sorted_boxes)
        max_heights = [0] * n
        for i in range(1, n):
            for j in range(i):
                if (sorted_boxes[j][0] <= sorted_boxes[i][0] and
                    sorted_boxes[j][1] <= sorted_boxes[i][1] and
                    sorted_boxes[j][2] <= sorted_boxes[i][2]):
                    max_heights[i] = max(max_heights[i], max_heights[j] + sorted_boxes[i][2])
        return max(max_heights)
