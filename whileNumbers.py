"""
Обратный порядок 2
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести число, записанное в обратном порядке.

Тестовые данные 🟢
Sample Input 1:

5086334
Sample Output 1:

4336805
Sample Input 2:

450098
Sample Output 2:

890054
Sample Input 3:

5088531157
Sample Output 3:

7511358805
"""

num = int(input())
while num != 0:
    last_num = num % 10
    print(last_num , end = '')
    num = num // 10