#N개의 점수의 평균(소수 첫째자리에서 반올림)을 구하고
#평균과 가장 가까운 점수의 인덱스 번호
#abs() 절대값

data = "40 73 66 87 92 67 75 79 75 80"
cnt = 0
index = 0
temp = 0
a = list(map(int, data.split()))
average =round((sum(a)/len(a)))
print(average)
for x in a:
    cnt = cnt+1
    if (abs(temp-average))>(abs(x-average)):
        temp = x
        index = cnt

print(index)