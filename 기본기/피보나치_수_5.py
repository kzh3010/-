n = int(input())+1
pi = [0] * n 
for i in range(n):
    if i == 0 or i == 1 :
        pi[i] = i 
    else :
        pi[i] = pi[i-1] + pi[i-2]
print(pi[n-1])

## 다른 사람 풀이
n = int(input())
dp = [0,1]
for i in range(1,n):
    dp.append(dp[i] + dp[i-1])
print(dp[n])