#개방 폐쇄의 원칙
import time

def time_decorator(func):
    def wrapper(*arg):
        s=time.time()
        r=func(*arg)
        e=time.time()
        print(f'실행시간 : {e-s}초')
        return r
    return wrapper


@time_decorator
def fatorial_repetition1(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

def fatorial_repetition(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

num=int(input('! 구하기: ' ))

#print(f'{num}! = {fatorial_repetition1(num)}')
print(fatorial_repetition1(num))
print("==")
x=time_decorator(fatorial_repetition)
print(x(num))
# 밑과 동일하지는 않다.(t_d는 위치값만 받지 전체를 처리하지 못함)
# print(time_decorator(fatorial_repetition(num)))
