# 연산자
print(1 + 1)  # 덧셈
print(3 - 2)  # 뺄셈
print(5 * 2)  # 곱셈은 X 대신 * 를 사용한다
print(6 / 3)  # 나눗셈은 결과값이 실수가 나온다
print()

print(2 ** 3)  # 2 ^ 3  = 8
print(5 % 3)  # 나눗셈의 나머지
print(5 // 3)  # 나눗셈의 몫
print()

print(10 > 3)  # True
print(4 >= 7)  # False
print(5 == 7)  # 비교하는 두 값이 같으면 True, 다르면 False 출력
print(1 != 6)  # 비교하는 두 값이 다르면 True, 같으면 False 출력
print(3 + 4 == 7)  # True
print(not (1 != 3))  # not True -> False
print()

print((3 > 0) and (3 < 5))  # 비교하는 두 값이 '모두' True여야 True 출력
print((3 > 0) & (3 < 5))  # and 대신 & 사용 가능
print((3 > 0) or (3 > 5))  # 비교하는 두 값 중 하나라도 True이면 True 출력
print((3 > 0) | (3 > 5))  # or 대신 | 사용 가능
print()

print(5 > 3 > 2)  # 연속적인 값들도 비교 가능
print(3 > 2 > 7)  # False


# 간단한 수식
print(2 + 3 * 4)  # 2 + 12 = 14
print((2 + 3) * 4)  # 5 * 4 = 20
print()

number = 2 + 3 * 4  # 14
print(number)
number = number + 2  # 16
print(number)  # 바뀐 number 값을 출력
number += 2  # number = number + 2 와 같은 식
print(number)  # 18
number *= 2  # 36
print(number)
number -= 2  # 34
print(number)
number /= 2  # 17
print(number)
number %= 5  # number를 5로 나눈 후 나머지 = 2
print(number)
print()


# 숫자처리함수
print(abs(-5))  # -5의 절대값인 5 출력
print(pow(4, 2))  # 4 ^ 2 = 16
print(max(5, 12))  # 최대값을 찾아 출력
print(min(5, 12))  # 최솟값을 찾아 출력
print(round(3.14))  #반올림한 값을 출력
print()

# python에서 제공하는 math library를 이용
from math import *
print(floor(4.99))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근


# 랜덤함수
from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 9 (정수만 출력하기 위해 int로 감싼다)
print(int(random() * 10 + 1))  # 1 ~ 10
print(randrange(1, 46))  # 1 ~ 45
print(randint(1, 45))  # 1 ~ 45


# Quiz)
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로, 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#
# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외
#
# 출력분 예제
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + "일로 선정되었습니다.")  # 이렇게도 가능