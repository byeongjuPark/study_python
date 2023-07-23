#k번째 큰 수 

data = "13 15 34 23 45 65 33 11 26 42"
k=3
a = list(map(int, data.split()))
a.sort()
a.reverse()
print(a[k-1])