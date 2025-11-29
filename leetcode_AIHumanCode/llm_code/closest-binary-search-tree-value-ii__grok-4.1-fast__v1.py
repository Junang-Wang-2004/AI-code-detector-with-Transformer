class Solution(object):
    def closestKValues(self, root, target, k):
        values = []
        curr = root
        path = []
        while curr or path:
            while curr:
                path.append(curr)
                curr = curr.left
            curr = path.pop()
            values.append(curr.val)
            curr = curr.right
        pivot = 0
        while pivot < len(values) and values[pivot] < target:
            pivot += 1
        l_idx = pivot - 1
        r_idx = pivot
        output = []
        for _ in range(k):
            if l_idx < 0:
                output.append(values[r_idx])
                r_idx += 1
            elif r_idx == len(values):
                output.append(values[l_idx])
                l_idx -= 1
            else:
                dist_l = abs(values[l_idx] - target)
                dist_r = abs(values[r_idx] - target)
                if dist_l <= dist_r:
                    output.append(values[l_idx])
                    l_idx -= 1
                else:
                    output.append(values[r_idx])
                    r_idx += 1
        return sorted(output)
