# 큐를 위해선 collections 모듈 이용해야(deque)
from collections import deque 

que = deque()
que.append(1)
que.append(2)
que.append(10)
que.append(5)
que.append(4)
print(que) # [1, 2, 10, 5, 4]
que.pop()
print(que) # [1, 2, 10, 5]
que.appendleft(11)
print(que) # [11, 1, 2, 10, 5]
que.append(12) 
print(que) # [11, 1, 2, 10, 5, 12]
que.popleft() 
print(que) # [1, 2, 10, 5, 12]
# print(que[::-1]) # typeError 
que = list(que)
print(que[::-1])