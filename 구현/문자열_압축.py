def solution(s):
    mid = len(s) // 2 
    result = len(s)
   
    for i in range(1,mid+1):
        count = 1
        ans = ''
        for k in range(0,len(s),i):
            if k == 0 :
                pre = s[k:i]
            else: 
                if pre == s[k:k+i]:
                    count += 1
                else :
                    ans += str(count) + pre if count >=2 else pre
                    count = 1
                    pre = s[k:k+i]
        
        ans += str(count) + pre if count >=2 else pre          
        result = min(result, len(ans))
                    
                
            
    return result





# 답지 풀이(이것이 취업을 코딩테스트다 with 파이썬)

def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1 
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count += 1
            else :
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer