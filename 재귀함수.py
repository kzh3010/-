# 재귀함수 자기 자신다시 호출
# 중요!! 종료 조건 명시해라 
def recur_func(i) :
    if i == 5 :
        return
    print(f"{i}번째 : ",i)
    recur_func(i+1)
    print(f"{i} 종료")
recur_func(1)

## 팩토리얼 재귀
def fac_func(n):
    if n <= 1 : ## 종료 조건 필수
        return 1 
    return n * fac_func(n-1)

print(fac_func(10))