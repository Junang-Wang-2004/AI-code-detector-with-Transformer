class Solution(object):
    def deserialize(self, s):
        def parse(pos):
            if s[pos] != '[':
                end = pos
                while end < len(s) and s[end].isdigit():
                    end += 1
                return NestedInteger(int(s[pos:end])), end
            node = NestedInteger()
            pos += 1
            while pos < len(s) and s[pos] != ']':
                elem, pos = parse(pos)
                node.add(elem)
                if pos < len(s) and s[pos] == ',':
                    pos += 1
            pos += 1
            return node, pos

        if not s:
            return NestedInteger()
        result, _ = parse(0)
        return result
