n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
result = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        value = a[i]
        countA = 0
        countB = 0
        
        while i < n and a[i] == value:
            countA += 1
            i += 1
        
        while j < m and b[j] == value:
            countB += 1
            j += 1
        
        result += countA * countB

print(result)
