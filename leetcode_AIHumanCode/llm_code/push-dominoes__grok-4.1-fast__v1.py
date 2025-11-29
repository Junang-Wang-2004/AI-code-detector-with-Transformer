class Solution:
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        dist_right = [n] * n
        dist_left = [n] * n
        pos_r = -1
        for i in range(n):
            if dominoes[i] == 'R':
                pos_r = i
            elif dominoes[i] == 'L':
                pos_r = -1
            else:
                if pos_r != -1:
                    dist_right[i] = i - pos_r
        pos_l = n
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                pos_l = i
            elif dominoes[i] == 'R':
                pos_l = n
            else:
                if pos_l != n:
                    dist_left[i] = pos_l - i
        result = []
        for i in range(n):
            if dominoes[i] != '.':
                result.append(dominoes[i])
            else:
                dr = dist_right[i]
                dl = dist_left[i]
                if dr < dl:
                    result.append('R')
                elif dr > dl:
                    result.append('L')
                else:
                    result.append('.')
        return ''.join(result)
