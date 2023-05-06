n = str(input())
mid = int(len(n)/2) 

left_count = 0 
right_count = 0 

for i in range(0,mid) :
    left_count += int(n[i]) 
for i in range(mid, len(n)) :
    right_count += int(n[i])

if left_count == right_count:
    print("LUCKY")
else :
    print("READY")


# 답지 풀이 (이것이 취업을 위한 코딩테스트다 with 파이썬)
n = input() 
length = len(n)
summary = 0 

for i in range(length // 2):
    summary += int(n[i])
for i in range(length // 2, length):
    summary -= int(n[i]) 

if summary == 0 :
    print("LUCKY")
else :
    print("READY")