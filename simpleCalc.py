a = int(input())
b = int(input())
c = str(input())

if c == '+':
    print(a + b)
elif c == '-':
   print(a - b)
elif c == '*':
   print(a * b) 
elif ((c == '/' or c == 'mod' or c == 'div') and b == 0):
   print('Деление на 0!')
elif c == '/': 
   print(a / b)
elif c == 'mod': 
   print(float(a % b))   
elif c == 'div': 
   print(float(a // b)) 
elif c == 'pow': 
   print(float(a ** b))
else:
  print('Введите корректно первое и второе цисло, а также верную оперцию над ними')