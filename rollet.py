a = int(input())

if a > 36 or a < 0:
    print('ошибка ввода')
elif a == 0:
    print('зеленый')
elif 1 <= a <= 10 and a % 2 == 0:
        print('черный') 
elif 1 <= a <= 10 and a % 2 != 0:
        print('красный')
elif 11 <= a <= 18 and a % 2 == 0:
        print('красный') 
elif 11 <= a <= 18 and a % 2 != 0:
        print('черный') 
elif 19 <= a <= 28 and a % 2 == 0:
        print('черный')  
elif 19 <= a <= 28 and a % 2 != 0:
        print('красный')        
elif 29 <= a <= 36 and a % 2 == 0:
        print('красный') 
elif 29 <= a <= 36 and a % 2 != 0:
        print('черный') 
