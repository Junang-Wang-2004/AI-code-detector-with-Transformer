class Solution(object):
    def decodeMessage(self, key, message):
        trans = {}
        nxt = ord('a')
        for ch in key:
            if 'a' <= ch <= 'z' and ch not in trans:
                trans[ch] = chr(nxt)
                nxt += 1
        return ''.join(trans.get(ch, ch) for ch in message)
