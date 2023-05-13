# https://www.acmicpc.net/problem/2501
n, k = map(int,input().split())
a = [i+1 for i in range(n)]
ans = []

for i in a :
    if n % i == 0:
        ans.append(i)
if len(ans) < k :
    print(0)
else:
    print(ans[k-1])

# 다른 사람 풀이 
n, k = map(int,input().split())
soo = [i for i in range(1, n+1) if n % i == 0]
print(soo[k-1] if len(soo) >= k else 0)
