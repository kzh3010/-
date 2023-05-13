## https://www.acmicpc.net/problem/3460
n = int(input())
for _ in range(n):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == "1":
            print(i, end = " ")

# 2진수 0b
# 8진수 0o
# 16진수 0x


## 다른 사람 풀이 

for _ in range(int(input())):
    n = int(input())
    cnt = 0 
    while n > 0 :
        if n % 2 == 1:
            print(cnt, end = " ")
        n = n // 2
        cnt += 1
