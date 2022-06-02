n = int(input())
i = n % 10
total = 0
while n > 0:
    num = n % 10
    if i != num:
        total += 1
        print('NO')
    n = n // 10
if total == 0:
    print('YES')