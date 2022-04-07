# if
# if 조건:
#   실행 명령문
# weather = input("오늘 날씨는? ")
# if weather == "비" or weather == "눈" or weather == "진눈깨비":
#     print("우산 챙기기")
# elif weather == "미세먼지":
#     print("마스크 챙기기")
# else:
#     print("준비물 필요 없음")
#
# temp = int(input("기온은? "))  # 사용자가 입력한 값을 정수로 변환해 temp에 저장
# if 30 <= temp:  # 기온 30도 이상
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:  # 기온 10~30도
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:    # 기온 0~10도
#     print("외투를 챙기세요")
# else:   # 기온 0도 이하
#     print("너무 추워요. 나가지 마세요")


# for
for waiting_no in [0, 1, 2, 3, 4]:  # list 내의 값들이 하나씩 돌아가면서 변수에 저장
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(5):  # 0, 1, 2, 3, 4
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(1, 6):  # 1, 2, 3, 4, 5
    print("대기번호: {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


# while: 어떤 조건문을 만족할 때까지 반복
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:  # 무한루프, 종료하려면 ctrl+c
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회.".format(customer, index))

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")  # 입력한 사람이 토르일 때 반복문 탈출, 아니면 반복문 계속 반복
# print("{0}, 커피가 준비 되었습니다.".format(person))



# continue, break
absent = [2, 5]  # 결석
no_book = [7]  # 책 안가져옴
for student in range(1, 11):  # 출석번호 1~10
    if student in absent:   # student가 absent에 포함되어 있다면, 즉 결석했다면
        continue    # 밑의 문장들을 실행하지 않고 위로 올라가서 반복문 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break   # 반복문에서 탈출
    print("{0}, 책을 읽어봐".format(student))  # absent인 2, 5를 제외하고 출력됨



# 한줄 for
students = [1, 2, 3, 4, 5]
print(students)  # [1, 2, 3, 4, 5]
students = [i+100 for i in students]  # students의 i를 하나씩 불러오면서 거기에 100을 더한 값을 list로 바꿔서 students에 집어넣음
print(students)  # [101, 102, 103, 104, 105]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]  # students의 값들을 하나씩 조회하면서 그 길이를 studetns에 집어넣음
print(students)  # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)  # ['IRON MAN', 'THOR', 'I AM GROOT']



# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객와 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1: 승객별 문행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요시간 5분~15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [o] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [o] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)
#
# 총 탑승 승객: 2 분

from random import *
cnt = 0  # 총 탑승 승객 수
for i in range(1, 51):  # 탑승객 1~50
    time = randrange(5, 51)  # 소요시간 5~50분 랜덤
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간: {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))
print("총 탑승 승객: {0} 분".format(cnt))
