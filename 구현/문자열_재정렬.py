## 문자도 sort로 하면 정렬이 되니까
n = input()

string = []
number = [] 

for i in n :
    if i.isdigit():
        number.append(int(i))
    else :
        string.append(i)
number_sum = sum(number)
string.sort()
string.append(str(number_sum))

print(''.join(string))

#  정답 풀이 (이것이 취업을 위한 코딩테스트다 with python)

data = input() 
result = [] 
value = 0 

for x in data : 
    if x.isalpha() : # 나의 경우 isdigit()을 답지는 isalpha()를 사용
        result.append(x)
    else:
        value += int(x) 

result.sort() 

if value != 0 :
    result.append(str(value))
print("".join(result))
