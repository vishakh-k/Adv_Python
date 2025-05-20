rows = 5
# Top half
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
# Bottom half
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
