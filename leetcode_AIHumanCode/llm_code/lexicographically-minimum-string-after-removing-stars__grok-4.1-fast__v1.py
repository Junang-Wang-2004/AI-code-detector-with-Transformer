class Solution:
    def clearStars(self, s: str) -> str:
        pos_stacks = [[] for _ in range(26)]
        for pos, char in enumerate(s):
            if char == '*':
                for st in pos_stacks:
                    if st:
                        st.pop()
                        break
            else:
                pos_stacks[ord(char) - ord('a')].append(pos)
        kept_pos = []
        for st in pos_stacks:
            kept_pos.extend(st)
        kept_pos.sort()
        return ''.join(s[p] for p in kept_pos)
