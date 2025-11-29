class Solution(object):
    def checkValidCuts(self, n, rectangles):
        def num_groups(projs):
            if not projs:
                return 0
            projs.sort(key=lambda t: t[0])
            groups = 1
            rightmost = projs[0][1]
            for left, right in projs[1:]:
                if left >= rightmost:
                    groups += 1
                    rightmost = right
                else:
                    rightmost = max(rightmost, right)
            return groups
        
        xproj = [(rec[0], rec[2]) for rec in rectangles]
        yproj = [(rec[1], rec[3]) for rec in rectangles]
        return num_groups(xproj) >= 3 or num_groups(yproj) >= 3
