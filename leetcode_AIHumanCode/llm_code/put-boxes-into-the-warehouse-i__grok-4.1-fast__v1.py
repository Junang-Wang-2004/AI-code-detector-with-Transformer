class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse):
        boxes.sort()
        min_height = float('inf')
        caps = []
        for height in warehouse:
            min_height = min(min_height, height)
            caps.append(min_height)
        box_ptr = 0
        num_placed = 0
        for i in range(len(caps) - 1, -1, -1):
            if box_ptr < len(boxes) and boxes[box_ptr] <= caps[i]:
                num_placed += 1
                box_ptr += 1
        return num_placed
