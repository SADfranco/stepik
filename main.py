# put your python code here
a = int(input()) 
s = []
for i in range(0,a):
  b,c = map(int, input().split())
  sum = b + c
  s.append(sum)    
print('\n'.join(map(str, s)))