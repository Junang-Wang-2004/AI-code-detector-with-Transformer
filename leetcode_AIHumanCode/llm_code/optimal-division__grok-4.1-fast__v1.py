class Solution(object):
    def optimalDivision(self, values):
        expr_parts = [str(val) for val in values]
        count = len(expr_parts)
        if count <= 2:
            return '/'.join(expr_parts)
        return expr_parts[0] + '/(' + '/'.join(expr_parts[1:]) + ')'
