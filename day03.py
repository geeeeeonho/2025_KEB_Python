import math


def my_pow(b,e) -> float:
    result = 1

    i=int(e)    #정수부분출력
    f=e-i       #소수부분출력

    for k in range(i):  #지수의 정수처리
        result=result*b

    if f>0:             #지수의 소수처리
        result=result*math.exp(f*math.log(b))
    return result

print(my_pow(2,10))
print(my_pow(4,0.5))
print(my_pow(25,0.5))