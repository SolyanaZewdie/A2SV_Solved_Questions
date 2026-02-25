t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ops = []
    

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append((3, i + 1))  # operation 3, 1-indexed
    

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                ops.append((1, j + 1))  # swap in a
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                ops.append((2, j + 1))  # swap in b
    
 
    print(len(ops))
    for op in ops:
        print(op[0], op[1])
