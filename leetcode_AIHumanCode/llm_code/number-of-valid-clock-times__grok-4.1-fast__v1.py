class Solution(object):
    def countTime(self, time):
        m_poss = (6 if time[3] == '?' else 1) * (10 if time[4] == '?' else 1)
        hh, hm = time[0], time[1]
        if hh == '?' and hm == '?':
            h_poss = 24
        elif hm == '?':
            h_poss = 4 if hh == '2' else 10
        elif hh == '?':
            h_poss = 3 if hm < '4' else 2
        else:
            h_poss = 1
        return h_poss * m_poss
