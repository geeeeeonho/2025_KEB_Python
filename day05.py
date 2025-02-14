import time
def time_decorator(func):
    """
    check time
    """
    def wrapper(*arg):
        s=time.time()
        r=func(*arg)
        e=time.time()
        print(f'실행시간 : {e-s}초')
        return r
    return wrapper



def timer_loop(n):
    for i in range(n):
        print(n-i)
    print('펑!!!')


def timer_recurs(n):
    if n < 0:
        return
    if n == 0:
        print('펑!!!')
    else:
        print(n)
    timer_recurs(n-1)



def case_timer_recurs(n):
    timer_recurs(n)


n=int(input("수 입력:"))
timer_loop(n)
timer_recurs(n)