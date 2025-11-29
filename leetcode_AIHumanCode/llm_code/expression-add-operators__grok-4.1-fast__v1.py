class Solution(object):
    def addOperators(self, num, target):
        result = []
        def dfs(idx, total, last, path):
            if idx == len(num):
                if total == target:
                    result.append(''.join(path))
                return
            num_val = 0
            for j in range(idx, len(num)):
                num_val = num_val * 10 + int(num[j])
                if num[idx] == '0' and j > idx:
                    break
                str_val = str(num_val)
                if idx == 0:
                    path.append(str_val)
                    dfs(j + 1, num_val, num_val, path)
                    path.pop()
                else:
                    # +
                    path.append('+')
                    path.append(str_val)
                    dfs(j + 1, total + num_val, num_val, path)
                    path.pop()
                    path.pop()
                    # -
                    path.append('-')
                    path.append(str_val)
                    dfs(j + 1, total - num_val, -num_val, path)
                    path.pop()
                    path.pop()
                    # *
                    path.append('*')
                    path.append(str_val)
                    new_total = total - last + last * num_val
                    new_last = last * num_val
                    dfs(j + 1, new_total, new_last, path)
                    path.pop()
                    path.pop()
        dfs(0, 0, 0, [])
        return result
