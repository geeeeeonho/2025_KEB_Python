def is_prime(n) -> bool:    #1.함수생성
    """
   check prime number
   if prime number return True
   if not prime number return False
    """
    if n >= 2:
        i=2
        while i <= int(n ** 0.5) :
            if n % i == 0:
                return False
                break
            i+=1
    else:
        return False
    return True


def is_prime_print(n):
    if is_prime(n):
        print(n," ",end="")

def range_prime(a,b):
    while a <= b:   #최소를 최대가 될 때까지 반복 입력
        is_prime(a)
        is_prime_print(a)
        a+=1
    print("\nis prime numbers in range")

num=input("range number(min max) :").split()    #띄어쓰기를 기준으로 구분
nmin=int(num[0])    #앞을 최소
nmax=int(num[1])    #뒤를 최대
range_prime(nmin,nmax)