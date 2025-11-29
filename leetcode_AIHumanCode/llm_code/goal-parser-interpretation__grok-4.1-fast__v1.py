class Solution:
    def interpret(self, command):
        ans = []
        ptr = 0
        n = len(command)
        while ptr < n:
            if command[ptr] == 'G':
                ans.append('G')
                ptr += 1
            elif command[ptr:ptr+2] == '()':
                ans.append('o')
                ptr += 2
            elif command[ptr:ptr+4] == '(al)':
                ans.append('al')
                ptr += 4
        return ''.join(ans)
