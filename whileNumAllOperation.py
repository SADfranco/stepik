"""
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

Тестовые данные 🟢
Sample Input 1:

5678
Sample Output 1:

26
4
1680
6.5
5
13
Sample Input 2:

132
Sample Output 2:

6
3
6
2.0
1
3
Sample Input 3:

75
Sample Output 3:

12
2
35
6.0
7
12
"""

num = int(input())
sum_num = 0
total = 0
multi = 1
last_num = num % 10
while num > 0:
    first_num = num % 10
    sum_num += first_num
    multi *= first_num
    total += 1
    num = num // 10
    
print(sum_num)
print(total)
print(multi)
print(sum_num/total)
print(first_num)
print(first_num + last_num)