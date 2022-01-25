# 문자열
sentence = '나는 말하는 감자다'
print(sentence)
sentence2 = "공부는 어렵다"
print(sentence2)
sentence3 = """
나는 말하는 감자이고, 
공부는 어렵다
"""
print(sentence3)

# 슬라이싱
potato = "970823-1234567"  # 임의로 설정한 주민등록번호
print("성별: " + potato[7])  # 7번째의 값을 가져옴(0부터 시작)
print("연: " + potato[0:2])  # 0번째부터 2번째 직전까지의 값을 가져옴
print("월: " + potato[2:4])  # 2번째 ~ 3번째
print("일: " + potato[4:6])  # 4번째 ~ 5번째

print("생년월일: " + potato[:6])  # 처음부터 6번째 직전까지
print("뒤 7자리: " + potato[7:])  # 7번째부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + potato[-7:])  # 맨뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 출력
print(python.upper())  # 대문자로 출력
print(python[0].isupper())  # 첫 번째 문자가 대문자이면 True 출력
print(len(python))  # 문자열의 길이
print(python.replace("Python", "Java"))  # python 문자열에서 python을 찾아 Java로 바꿈

index = python.index("n")  # python 문자열에서 n이 몇번째에 있는지 출력
print(index)  # 첫번째 n의 위치
index = python.index("n", index + 1)  # 아까처럼 python 문자열에서 n을 찾는데 위에서 찾은 위치에서 1을 더한 위치에서부터 찾음
print(index)  # 두번째 n의 위치

print(python.find("Java"))  # 찾는 문자가 없으면 -1 출력
# print(python.index("Java"))  # 찾는 문자가 없으면 에러 발생

print(python.count("n"))  # 문자열에서 n이 몇 번 나오는 지 출력

# 문자열 포멧
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)  # % 뒤의 값을 %d(정수값만 가능)에 넣음
print("나는 %s를 좋아해요." % "파이썬")  # 문자열 파이썬
print("Apple은 %c로 시작해요." % "A")  # 문자 A
print("나는 %s살이고 %s를 좋아해요." % (20, "딸기"))  # %s는 문자열뿐만 아니라 숫자와 문자도 넣을 수 있다

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4 (ver 3.6~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견\n벡견이 불여일타")  # \n: 줄바꿈
print("저는 \'나도코딩\' 입니다.")  # \': ' 출력
print("저는 \"나도코딩\" 입니다.")  # \": " 출력

print("C:\\Users\\70160\\PycharmProjects")  # \\: \출력

print("Red Apple\rPine")  # \r: 커서를 맨 앞으로 이동
  # Red Apple을 적고 커서를 맨 앞으로 이동시켜 "Red "에 "Pine" 덮어씀

print("Redd\bApple")  # \b: 백스페이스 (한 글자 삭제)

print("Red\tApple")  # \t: 탭


# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1: http:// 부분은 제외 -> naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 \
# (nav) + (5) + (1) + (!)
# -> 생성된 비밀번호: nav51!

url = "http://naver.com"
# print(url)
my_str = url.replace("http://", "")  # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")]  # 규칙2
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "1"
# print(password)
print(f"{url}의 비밀번호는 {password}입니다.")