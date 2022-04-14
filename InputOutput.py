# 표준 입출력
print("Python", "Java", sep = " vs ", end="?")
# "," 에 " vs " 출력 & 문장의 끝부분을 "?"로 바꿈, 뒷문장 연달아 출력
print("무엇이 더 재미있을까요?")  # Python vs Java?무엇이 더 재미있을까요? <- 한줄로 출력됨

import sys
print("Python", "Java", file=sys.stdout)  # 표준 출력
#print("Python", "Java", file=sys.stderr)  # 표준 에러

# 시험성적
scores = {"수학":0, "영어":50, "코딩":100}  # 사전
for subject, score in scores.items():  # .items()를 사용하면 key와 value를 쌍으로 tuple로 보내줌
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # subject는 총 8칸의 공간을 가진채로 왼쪽정렬, score는 총 4칸의 공간을 가진채로 오른쪽 정렬
    # 수학      :   0
    # 영어      :  50
    # 코딩      : 100

# 은행 대기 순번표 (001, 002, 003, ...)
for num in range(1, 21):  # 1 ~ 21
    print("대기번호: " + str(num).zfill(3))
    # 3칸의 공간을 확보한 채 값을 집어넣는데 값이 없는 빈 공간에는 0으로 채움
    # 대기번호: 001
    # 대기번호: 002
    # 대기번호: 003 ...

# answer = input("아무 값이나 입력하세요: ")
# input안의 문장 출력후 입력 대기, 입력값이 문자열 형태로 answer에 들어감
# 사용자 입력을 통해서 값을 갖게 되면 항상 문자열 형태로 저장됨
# print("입력하신 값은 " + answer + "입니다.")



# 다양한 출력포맷

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))  #        500
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))  #       +500
print("{0: >+10}".format(-500))  #       -500

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))  # 500_______

# 3자리 마다 콤마 찍기
print("{0:,}".format(100000000000))  # 100,000,000,000
# 3자리 마다 콤마 찍기 & +- 부호 붙이기
print("{0:+,}".format(100000000000))  # +100,000,000,000
print("{0:+,}".format(-100000000000))  # -100,000,000,000
# 3자리 마다 콤마를 찍기 & 부호 붙이기 & 자릿수 확보 & 빈자리는 ^로 채우기
print("{0:^<+30,}".format(100000000000))  # +100,000,000,000^^^^^^^^^^^^^^

# 소수점 출력
print("{0:f}".format(5/3))  # 1.666667
print("{0:.2f}".format(5/3))  # 1.67



# 파일 입출력
# 파일을 열어서 점수 정보를 쓰기
score_file = open("score.txt", "w", encoding="utf8")  # encoding="utf8"는 한글 깨지는 것 방지
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()
# score_file을 쓰기 목적으로 열어서(score.txt 생성) 내용을 파일에 쓰고 파일을 닫음

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 88")  # 줄바꿈 따로 안해줌
score_file.write("\n코딩: 100")
score_file.close()

# 파일에 있는 내용 읽어오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())  # 파일에 있는 모든 내용을 읽어와 출력
score_file.close()
 # 수학: 0
 # 영어: 50
 # 과학: 88
 # 코딩: 100

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(),end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 | end="" 사용할 경우 줄바꿈X
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

# file을 읽어올 때 파일 안에 내용이 얼마나 들어있는지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:  # 무한루프
    line = score_file.readline()
    if not line:  # 읽어온 내용이 없으면 반복문 탈출
        break
    else:
        print(line, end="")
score_file.close()

# list에 값을 넣어 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 line을 읽어와 list 형태로 저장
for line in lines:
    print(line, end="")  # list에서 한 줄씩 불러와 출력
score_file.close()
print()



# pickle: 프로그램 상에서 우리가 사용하고 있는 데이터를 파일형태로 저장
import pickle
profile_file = open("profile.pickle", "wb")
# 쓰기목적으로 w로 정의, pickle을 사용하기 위해서 항상 binary type을 정의해줘야 하기 때문에 "wb"로 씀
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 저장
profile_file.close()
  # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

profile_file = open("profile.pickle", "rb")  # 읽기 목적
profile = pickle.load(profile_file)  # profile_file의 정보를 profile에 불러옴
print(profile)
profile_file.close()
  # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
  # 정리하면 우리가 가지고 있는 데이터(박명수~)를 pickle을 이용해서 파일(profile_file)에 저장하고
  # 그 파일에 있는 내용을 load를 통해서 불러와 변수에 저장해 사용함



# with
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
  # profile 파일을 읽기 전용으로 열어서 profile_file 변수에 저장해두고
  # 파일의 내용을 pickle.load()를 통해 불러와서 출력
  # with을 사용할 경우 자동으로 파일을 닫기 때문에 close() 쓸 필요가 없다.

# pickle 사용하지 않고 with를 사용해 파일 열고 닫기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
  # study.txt를 생성해 쓰기 목적으로 열고 변수 study_file에 저장

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())  # study_file의 내용을 read()를 사용해 읽어옴
    # 파이썬을 열심히 공부하고 있어요



# Quiz) 당신의 회사에서는 매주 1회 작성해여 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#
# - X 주차 주간보고 -
# 부서 :
# 이름:
# 업무 요약:
#
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
#
# 조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

for n in range (1, 51):
    with open("{0}주차.txt".format(n), "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - ".format(n))
        report_file.write("\n부서 : ")
        report_file.write(("\n이름 : "))
        report_file.write(("\n업무요약: "))

# for n in range (1, 51):
#     with open("{0}주차.txt".format(n), "r", encoding="utf8") as report_file:
#         print(report_file.read())

# X주차.txt 쓰는 다른 방법
# open(str(i) + "주차.txt")