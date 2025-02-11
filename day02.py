#구구단
# for dan in range(2,10):
#     for i in range(1,10):
#         print(f"{dan}*{i}={dan*1}")

#입력받은 구구단만 출력
# dan = int(input("Input dan :"))
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")

#입력 소수 확인하기(루트 범위로 줄이기)
def is_prime(n) -> bool:    #1.함수생성
    """
   check prime number
   if prime number return True
   if not prime number return False
    """
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):  # n의 0.5승을 int로
            if n % i == 0:
                return False
                break
    else:
        return False
    return True

n=int(input("input number :"))

if is_prime(n):
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")

def help(is_prime):
    print('''소수를 판정하는 함수
    소수면 true를, 소수가 아니면 false를 리턴함''')