N = int(raw_input())
P = [int(raw_input()) for _ in range(N)]
T = [0]*(N+1)
for p in P:
  T[p] = T[p-1]+1
print N-max(T)
