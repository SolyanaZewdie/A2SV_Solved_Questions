def solve(index, current):
    if index == len(s2):
        if current == target:
            return 1
        return 0

    if s2[index] == '+':
        return solve(index + 1, current + 1)

    elif s2[index] == '-':
        return solve(index + 1, current - 1)

    else:
        return solve(index + 1, current + 1) + solve(index + 1, current - 1)


k = s2.count('?')
total = 2 ** k

valid = solve(0, 0)

print("{:.12f}".format(valid / total))