# import color
num = int(input())
total = 0
while num != 0:
    if num >= 25:
        num -= 25
        total += 1
    if 10 <= num < 25:
        num -= 10
        total += 1
    if 5 <= num < 10:
        num -= 5
        total += 1   
    if 1 <= num < 5:
        num -= 1
        total += 1        

print(total)