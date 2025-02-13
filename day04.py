#개방 폐쇄의 원칙
import time

def fatorial_repetition(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

num=int(input( ))
s=time.time()
print(f'{num}! = {fatorial_repetition(num)}')
e=time.time()
print(e-s)