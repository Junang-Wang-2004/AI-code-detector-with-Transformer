h, w, k = map(int, raw_input().split())
mod = 1000000007

def check(s):
	for i in xrange(1, w):
		if (((s>>i)&1) and ((s>>(i-1))&1)):
			return False
	return True

dp = [[0] * 101 for _ in xrange(101)]

nxt = 0
dp[0][0] = 1;
for i in xrange(1, h+1):
	for pre in xrange(0, w):
		for mask in xrange(0, 1<<(w-1)):
			if check(mask):
				if (((1)&(mask>>pre)) == 1):
					nxt = pre + 1
				elif (pre > 0 and ((mask>>(pre-1))&1) == 1):
					nxt = pre - 1
				else:
					nxt = pre
				dp[i][nxt] += dp[i-1][pre]
				dp[i][nxt] %= mod

print dp[h][k-1]
