t=int(input())
for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    s=0
    mr=0
    for x in r:
        s+=x
        if s>mr:
            mr=s
    s=0
    mb=0
    for x in b:
        s+=x
        if s>mb:
            mb=s
    print(mr+mb)
