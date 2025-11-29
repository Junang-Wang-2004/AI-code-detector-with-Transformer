S = raw_input()
T = raw_input()
d = dict()
d2 = dict()
ret = True
for s, t in zip(S, T):
    if s in d and d[s] != t:
        ret = False
        break
    if t in d2 and d2[t] != s:
        ret = False
        break
    d[s] = t
    d2[t] = s
        
print 'Yes' if ret else 'No'
