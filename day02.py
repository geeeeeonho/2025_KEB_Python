#구구단
# for dan in range(2,10):
#     for i in range(1,10):
#         print(f"{dan}*{i}={dan*1}")

#입력받은 구구단만 출력
# dan = int(input("Input dan :"))
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")

#입력 소수 확인하기(루트 범위로 줄이기)
n=int(input("input number :"))
is_prime = True     #소수 판별 변수(참, 거짓)

if n>=2:
    for i in range(2, int(n**0.5)+1):    #n의 0.5승을 int로
        if n%i==0:
            is_prime = False    #하나라도 나눠지면 거짓
            break
else:
    is_prime = False

if is_prime:
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")