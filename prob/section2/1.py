#K번째 약수
n = 6
k = 3

a = list()
for x in range(1, n):
    if(n % x == 0):
        a.append(x)

if len(a)<k:
    print(-1)
else:
    print(a[k-1])