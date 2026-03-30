s = input().strip()

stack = [-1]
max_len = 0
count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1

if max_len == 0:
    print("0 1")
else:
    print(max_len, count)