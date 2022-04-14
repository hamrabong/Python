# 함수
# def 함수이름():
#    실행문
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()  # 함수 호출


# 전달값과 반환값
def deposit(balance, money):  # 입금 (잔액: balance, 입금액: money)
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money  # 원하는 값 반환


def withdraw(balance, money):  # 출금 (잔액: balance, 출금액: money)
    if balance >= money:  # 잔액이 출금액 보다 많아랴 출금 가능
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission  # 여러개의 값을 한번에 반환 가능


balance = 0
balance = deposit(balance, 1000)  # deposit 함수 호출해 1000원 입금
balance = withdraw(balance, 2000)  # 출금액이 잔액보다 커서 출금 불가
balance = withdraw(balance, 500)  # 500원 출금
commission, balance = withdraw_night(balance, 200)  # 수수료 100원, 출금액 200원으로 총 300원 출금
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))  # 수수료는 100원이며, 잔액은 200원 입니다.


# 기본값
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
          .format(name, age, main_lang))  # 역슬래시 치고 엔터 누르면 두문장이지만 한문장으로 처리됨

profile("유재석", 20, "파이썬")  # 이름: 유재석	나이: 20	주 사용 언어: 파이썬
profile("김태호", 25, "자바")  # 이름: 김태호	나이: 25	주 사용 언어: 자바

# 같은 나이 같은 주 사용 언어
def profile(name, age = 17, main_lang = "파이썬"):  # 값을 전달받지 않았을 경우 기본값 사용
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
          .format(name, age, main_lang))

profile("유재석")  # 이름: 유재석	나이: 17  주 사용 언어: 파이썬
profile("김태호")  # 이름: 김태호	나이: 17  주 사용 언어: 파이썬



# 키워드 값을 이용한 함수 호출
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
#함수에서 전달받는 매개변수의 값을 키워드를 이용해서 함수로 호출하면 그 키워드에 해당하는 값이 순서가 뒤섞여있어도 잘 전달된다.



# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")  # end=" " 는 이 print문이 끝날때 줄바꿈을 하지 않음
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")  # 이름: 유재석	나이: 20	 Python Java C C++ C#
profile("김태호", 25, "Kotlin", "Swift", "", "", "")  # 2가지 언어만 알아서 빈값을 넣음

def profile2(name, age, *language):  # 내가 넣고싶은 만큼 값을 넣을 수 있음
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")  # end=" " 는 이 print문이 끝날때 줄바꿈을 하지 않음
    for lang in language:
        print(lang, end=" ")
    print()

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile2("김태호", 25, "Kotlin", "Swift")  # 빈 값 넣을 필요 없음



# 지역변수와 전역변수
# 지역변수: 함수 내에서만 쓸 수 있고 함수가 호출될 때 만들어졌다가 호출이 끝나면 사라짐
# 전역변수: 프로그램 내에서 어디서든 부를 수 있는 변수
gun = 10
def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers  # gun 변수는 지역변수, 초기화해야 사용 가능
    print("[함수 내] 남은 총: {0}".format(gun))  # [함수 내] 남은 총: 18

print("전체 총: {0}".format(gun))  # 전체 총: 10
checkpoint(2)  # 2명이 겅계근무
print("남은 총: {0}".format(gun))  # 남은 총: 10

def checkpoint2(soldiers):
    global gun  # 전역 공간에 있는 gun 변수 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))  # [함수 내] 남은 총: 8

print("전체 총: {0}".format(gun))  # 전체 총: 10
checkpoint2(2)  # 2명이 겅계근무
print("남은 총: {0}".format(gun))  # 남은 총: 8

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers  # 지역변수
    print("[함수 내] 남은 총: {0}".format(gun))  # [함수 내] 남은 총: 6
    return gun  # 함수 밖의 변수의 값 바꿈

print("전체 총: {0}".format(gun))  # 전체 총: 8
gun = checkpoint_return(gun, 2)
print("남은 총: {0}".format(gun))  # 남은 총: 6


# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
#
# * 표준체중: 각 개인의 키에 적당한 체중
# 성별에 따른 공식)
#
# 남자: 키(m) * 키(m) * 22
# 여자: 키(m) * 키(m) * 21
#
# 조건1: 표준 체중은 별도의 함수 내에서 계산
#     함수명: std_weight
#     전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시
#
# 출력예제) 키 175cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender):
    if gender == "남자":
        weight = height * height * 22
        return weight
    else:
        weight = height * height * 21
        return weight

weight = std_weight(1.75, "남자")
print("키 175cm 남자의 표준 체중은 {:.2f}kg입니다.".format(weight))

