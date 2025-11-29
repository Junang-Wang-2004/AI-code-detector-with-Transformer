n = int(raw_input())
s1 = raw_input()
s2 = raw_input()
used = 0
pat = 1
i = 0
while i < n:
    if s1[i] == s2[i]:
        pat = pat*(3 - used) % (10**9+7)
        used = 1
        i += 1
    else:
        if used == 0:
            pat = pat*6 % (10**9+7)
        else:
            pat = pat*(used + 1) % (10**9+7)
        used = 2
        i += 2
print pat
