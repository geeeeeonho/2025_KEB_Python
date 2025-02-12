import random

df=[ ["위스키","초콜릿"] , ["와인","치즈"] , ["소주","삽겹살"] , ["고량주","양꼬치"]]
jf=["사케","광어회"]

df.append(jf)
df[0][1]="낙곱새"

def recommand(n):    #메뉴 추천
    print(f'{df[n - 1][0]}에 어울리는 안주는 {df[n- 1][1]} 입니다')

while True:
    try:
        menu = int(input(f'다음 술중에 고르세요.\n1) {df[0][0]}   2) {df[1][0]}   3) {df[2][0]}   4) {df[3][0]}   5) {df[4][0]}   6) 아무거나   7) 종료 : '))
    except:
        print("잘못된 입력입니다.")
        continue
    if menu in range(1,6):
        recommand(menu)
    elif menu == 6:
        random_menu = random.randint(1,len(df))
        recommand(random_menu)
    elif menu == 7:
        print(f'다음에 또 오세요')
        break