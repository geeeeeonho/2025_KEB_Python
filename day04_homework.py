# SOLID
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)
import time


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper


def description_decorator(func):  # closure
    def wrapper(*arg):
        print(func.__name__)    #이름
        print(func.__doc__)     #설명(""""""안에 있는 내용 출력)
        r = func(*arg)  #실제 오리지널 함수를 실행시킬 코드
        return r

    return wrapper



@time_decorator
@description_decorator
def factorial_repetition(n) -> int:
    """
    make factorial by loop
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input("! 구하기:"))
print(f"{number}! = {factorial_repetition(number)}")