class Solution:
    def generate(self, numRows):
        triangle = []
        for level in range(numRows):
            row = [1] * (level + 1)
            for idx in range(1, level):
                row[idx] = triangle[level - 1][idx - 1] + triangle[level - 1][idx]
            triangle.append(row)
        return triangle
