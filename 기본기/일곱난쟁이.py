a = []
for _ in range(9):
    a.append(int(input()))
hei = []
for i in range(0,3):
    hei = [a[i]]
    for j in range(i+1,9):
        hei.append(a[j]) 
        if sum(hei) == 100:
            hei.sort()
            break 
for i in hei :
    print(i)
        