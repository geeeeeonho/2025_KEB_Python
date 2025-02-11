#구구단
# for dan in range(2,10):
#     for i in range(1,10):
#         print(f"{dan}*{i}={dan*1}")

#입력받은 구구단만 출력
# dan = int(input("Input dan :"))
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")

#소수 확인하기
count = 0
num=int(input("input number :"))
for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print(f"{num} is prime number.")
else:
    print(f"{num} is not prime number.")