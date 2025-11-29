class Solution:
    def findPeakGrid(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        if rows > cols:
            left = 0
            right = rows - 1
            while left < right:
                mid = (left + right) // 2
                if max(mat[mid]) > max(mat[mid + 1]):
                    right = mid
                else:
                    left = mid + 1
            peak_r = left
            mx = mat[peak_r][0]
            peak_c = 0
            for j in range(1, cols):
                if mat[peak_r][j] > mx:
                    mx = mat[peak_r][j]
                    peak_c = j
            return [peak_r, peak_c]
        else:
            def colmax(jj):
                mx = mat[0][jj]
                for ii in range(1, rows):
                    if mat[ii][jj] > mx:
                        mx = mat[ii][jj]
                return mx
            left = 0
            right = cols - 1
            while left < right:
                mid = (left + right) // 2
                if colmax(mid) > colmax(mid + 1):
                    right = mid
                else:
                    left = mid + 1
            peak_c = left
            mx = mat[0][peak_c]
            peak_r = 0
            for i in range(1, rows):
                if mat[i][peak_c] > mx:
                    mx = mat[i][peak_c]
                    peak_r = i
            return [peak_r, peak_c]
