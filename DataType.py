# 숫자 자료형
print(5)  # 숫자를 직접 출력할 수 있다.
print(-10)  # 음수도 마찬가지
print(3.14)  # 실수
print(5 + 3)  # 덧셈후 결과값을 출력하는 것도 가능하다.
print(2 * 5)  # 곱셈은 X 대신 * 을 사용한다.
print(3 * (3 + 1))  # 괄호도 사용가능


# 문자열 자료형
print('풍선')
print("나비")
print("animal")
print("ㅋ" * 9)  # 문자열과 정수를 섞어서 계산한 후 출력할 수도 있음


# boolean(참/거짓) 자료형
print(5 > 10)  # False
print(5 < 10)  # True
print(True)
print(False)
print(not True)  # False
print(not (5 > 10))  # not False -> True


# 변수
animal = "강아지"  # 문자열
name = "연탄이"  # 문자열
age = 4  # 정수형 자료
hobby = "산책"
is_adult = (age >= 3)  # age가 3 이상이면 adult

print("우리집" + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")  # 정수형을 출력할 때 문자열로 바꾸기 위해 str로 감싸준다 (아니면 오류 발생)
print(name, "는 ", age, "살이며, ", hobby, "를 아주 좋아해요")  # + 대신 , 로 사용가능 이때 str 필요없이 바로 age 쓸 수 있다
print(name + "는 어른일까요? " + str(is_adult))  # boolean도 정수형과 마찬가지로 문자열로 바꾸어서 출력해야함


# 주석: 프로그램 내에 포함은 되어 있으나 실제로 실행은 되지 않는 문장

''' 작은 따옴표 3개를 앞뒤로 붙이면 
여러문장이 주석처리 된다 '''
# 여러문장을 선택 후 ctrl + / 를 누르면 한번에 주석처리 된다.
# 주석처리를 해제하려면 마찬가지로 ctrl + / 를 누른다.


# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명: station
# 변수값: "사당", "신도림", "인천공항" 순서대로 입력 
# 출력문장: XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
