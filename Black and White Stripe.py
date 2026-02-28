import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    white = 0
    for i in range(k):
        if s[i] == 'W':
            white += 1
    
    answer = white
    
    for i in range(k, n):
        if s[i] == 'W':
            white += 1
        if s[i - k] == 'W':
            white -= 1
        
        answer = min(answer, white)
    
    print(answer)
