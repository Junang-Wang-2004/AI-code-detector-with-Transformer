class Solution(object):
    def lengthLongestPath(self, input):
        stack = [0]
        max_path = 0
        for line in input.splitlines():
            depth = 0
            pos = 0
            while pos < len(line) and line[pos] == '\t':
                depth += 1
                pos += 1
            name_len = len(line) - pos
            while len(stack) > depth + 1:
                stack.pop()
            path_len = stack[-1] + name_len
            if '.' in line[pos:]:
                max_path = max(max_path, path_len)
            else:
                stack.append(path_len + 1)
        return max_path
