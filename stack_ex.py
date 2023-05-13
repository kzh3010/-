stack = []

# 선입 후출
stack.append(4)
stack.append(3)
stack.append(2)
stack.append(1)
stack.append(10)
stack.append(23)
stack.pop() ## 23
stack.pop() ## 10 

# 데이터 가져오기
print(stack)  # [4,3,2,1]
print(stack[::-1]) # [1,2,3,4] 