person = 0
sub = []  
for _ in range(10):
    x, y = map(int,input().split())
    person = person - x + y  
    sub.append(person)
print(max(sub))


## 다른 사람 풀이 
max = 0 
person = 0 
for i in range(10):
    a, b = map(int,input().split())
    person = person - a + b 
    if person > max : 
        max = person 
print(max)