import random

df=[ ["위스키","초콜릿"] , ["와인","치즈"] , ["소주","삽겹살"] , ["고량주","양꼬치"]]
jf=["사케","광어회"]

df.append(jf)
df[0][1]="낙곱새"

def recommand(n):    #메뉴 추천
    print(f'{df[n - 1][0]}에 어울리는 안주는 {df[n- 1][1]} 입니다')


menu_list='다음 술 중에 고르세요.\n'
i=0
for i in range(1,len(df)+1):
    menu_list=menu_list+f'{i}) {df[i-1][0]}   '
menu_list=menu_list+f'{i+1}) 아무거나   {i+2}) 종료   :'

while True:
    try:
        menu = int(input(menu_list))    #입력받은 술 번호(menu)는 실제위치보다 1 많다.
    except:
        print("잘못된 입력입니다.")
        continue
    if menu in range(1,i+1):
        recommand(menu)
    elif menu == i+1:
        random_menu = random.randint(1,len(df))
        recommand(random_menu)
    elif menu == i+2:
        print(f'다음에 또 오세요')
        break