t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))
    left_colors = {}
    right_colors = {}
    for i in range(l):
        left_colors[c[i]] = left_colors.get(c[i], 0) + 1
    for i in range(l, n):
        right_colors[c[i]] = right_colors.get(c[i], 0) + 1

    for color in list(left_colors.keys()):
        if color in right_colors:
            m = min(left_colors[color], right_colors[color])
            left_colors[color] -= m
            right_colors[color] -= m
            if left_colors[color] == 0:
                del left_colors[color]
            if right_colors[color] == 0:
                del right_colors[color]

    left_remain = sum(left_colors.values())
    right_remain = sum(right_colors.values())
    cost = 0

    if left_remain > right_remain:
        left_colors, right_colors = right_colors, left_colors
        left_remain, right_remain = right_remain, left_remain

    diff = right_remain - left_remain
    for color in list(right_colors.keys()):
        while right_colors[color] >= 2 and diff > 0:
            right_colors[color] -= 2
            diff -= 2
            cost += 1

    cost += diff // 2
    cost += (sum(left_colors.values()) + sum(right_colors.values())) // 2
    print(cost)
