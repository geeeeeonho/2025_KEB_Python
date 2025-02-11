def is_prime(n) -> bool:    #1.함수생성
    """
   check prime number
   if prime number return True
   if not prime number return False
    """
    if n >= 2:
        i=2
        while i <= (int(n ** 0.5) +1) :
            if n % i == 0:
                return False
                break
            i+=1
    else:
        return False
    return True
n=int(input("input number :"))
if is_prime(n):
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")