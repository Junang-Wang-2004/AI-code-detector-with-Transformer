class Solution(object):
    def minMovesToCaptureTheQueen(self, rx, ry, qx, qy, bx, by):
        row_shared = rx == bx
        queen_on_row = qx == rx
        sides_row = (ry - qy) * (by - qy) < 0
        check_row = row_shared and not (queen_on_row and sides_row)

        col_shared = ry == by
        queen_on_col = qy == ry
        sides_col = (rx - qx) * (bx - qx) < 0
        check_col = col_shared and not (queen_on_col and sides_col)

        antidiag_qb = qx + qy == bx + by
        antidiag_wx = rx + ry == qx + qy
        sides_adiag = (qx - rx) * (bx - rx) < 0
        check_adiag = antidiag_qb and not (antidiag_wx and sides_adiag)

        diag_qb = qx - qy == bx - by
        diag_wx = rx - ry == qx - qy
        sides_diag = (qy - ry) * (by - ry) < 0
        check_diag = diag_qb and not (diag_wx and sides_diag)

        if check_row or check_col or check_adiag or check_diag:
            return 1
        return 2
