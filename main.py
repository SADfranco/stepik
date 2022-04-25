# import color
import math
a,b,c = float(input()),float(input()),float(input())
D = b**2-4*a*c
x = (((-b+math.sqrt(D))/2*a),((-b-math.sqrt(D))/2*a))
if D > 0:
    print(min(x))
    print(max(x))        
elif D == 0:
    print(-b/2*a)
else:
    print("Нет корней")