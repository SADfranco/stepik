"""Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. При смешивании двух основных цветов получается вторичный цвет:

если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который получится в результате.

Формат входных данных
На вход программе подаются две строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

Примечание 1. Если смешать красный и красный, то получится красный и т.д.

Примечание 2. Поиграйтесь с настоящим цветовым микшером 🙂"""


a = str(input())
c = str(input())
b = 'зеленый желтый красный синий'


if a == 'красный' and c == 'синий' or c == 'красный' and a == 'синий':
    print('фиолетовый')
elif a == 'красный' and c == 'желтый' or c == 'красный' and a == 'желтый':
    print('оранжевый')
elif c == 'синий' and a == 'желтый' or a == 'синий' and c == 'желтый' :
    print('зеленый')
elif a not in b:
    print('ошибка цвета')
elif a == c:
    print(a)
else:
    print('ошибка цвета')