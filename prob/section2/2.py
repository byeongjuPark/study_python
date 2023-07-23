#오름 차순 정렬 후 K번째의 수

data = "6 2 5 3"
k = 2
a = list(map(int, data.split()))
a.sort()
print(a[k-1])

