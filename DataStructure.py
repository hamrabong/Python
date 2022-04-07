# 리스트 [] : 순서를 가지는 객체의 집합
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]  # 리스트를 사용함으로써 위의 3줄을 한줄로 줄임
print(subway)  # [10, 20, 30]

subway = ["A", "B", "C"]
print(subway)  # ['A', 'B', 'C']

# B가 몇 번째 칸에 타고있는지 출력
print(subway.index("B"))  # 1

subway.append("D")  # D가 다음 칸에 탐
print(subway)  # ['A', 'B', 'C', 'D']

subway.insert(1, "E")  # E를 1번째 자리(0번째 자리 뒤)에 삽입, 나머지 값들은 하나씩 뒤로 밀림
print(subway)  # ['A', 'E', 'B', 'C', 'D']

# 맨 뒤의 원소를 뺌
print(subway.pop())  # D (뺀 원소 출력)
print(subway)  # ['A', 'E', 'B', 'C']

# 같은 원소가 몇 개 있는지
subway.append("A")
print(subway)  # ['A', 'E', 'B', 'C', 'A']
print(subway.count("A"))  # 2

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)  # [1, 2, 3, 4, 5]

# 순서 뒤집기
num_list.reverse()
print(num_list)  # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list)  # []

# 리스트는 자료형에 구애받지 않고 다양한 자료형과 함께 사용 가능
mix_list = ["KIM", 15, True]
print(mix_list)  # ['KIM', 15, True]

# 리스트 확장 (하나의 리스트로 합침)
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)  # [5, 2, 4, 3, 1, 'KIM', 15, True]

# 사전 (key와 value형태로 나뉨, key 중복X)
# {key:"value"} 식으로 구성
cabinet = {3: "KIM", 100: "LEE"}
print(cabinet[3])  # KIM (cabinet의 key값에 대응하는 value값 출력)
print(cabinet[100])  # LEE

print(cabinet.get(3))  # KIM
# print(cabinet[5])  # cabinet에 5라는 key값이 없기 때문에 오류 발생
print(cabinet.get(5))  # 값이 없어도 None을 출력, 오류발생X
print(cabinet.get(5, "사용 가능"))  # 일단 cabinet에서 5에 대응하는 값을 가져오려고 시도하고, 없으면 "사용 가능" 출력

# 사전 자료형 안에 어떤 값이 있는지 확인하는 방법
# key in variable
print(3 in cabinet)  # True (3이라는 key값이 cabinet에 존재)
print(5 in cabinet)  # False (5라는 key값이 cabinet에 존재X)

# 정수가 아닌 string도 key값으로 사용 가능
cabinet = {"A-3": "spring", "B-100": "summer"}
print(cabinet["A-3"])  # spring
print(cabinet["B-100"])  # summer

# 새로운 key와 value값 추가 및 value값 변경
print(cabinet)  # {'A-3': 'spring', 'B-100': 'summer'}
cabinet["A-3"] = "winter"
cabinet["c-20"] = "fall"
print(cabinet)  # {'A-3': 'winter', 'B-100': 'summer', 'c-20': 'fall'}

# value값 지우기
# del variable[key]
del cabinet["A-3"]
print(cabinet)  # {'B-100': 'summer', 'c-20': 'fall'}

# key 들만 출력
print(cabinet.keys())  # dict_keys(['B-100', 'c-20'])

# value 들만 출력
print(cabinet.values())  # dict_values(['summer', 'fall'])

# key, value 쌍으로 출력
print(cabinet.items())  # dict_items([('B-100', 'summer'), ('c-20', 'fall')])

# 변수 안의 모든 값들 지우기
cabinet.clear()
print(cabinet)  # {}

# 튜플 (리스트와는 다르게 내용 변경/추가 불가능, 속도 빠름)
# 변경되지 않는 목록을 사용할 때 활용
# variable = ("value", "value", ...) 형태
menu = ("돈까스", "치즈까스")
print(menu[0])  # 돈까스
print(menu[1])  # 돈까스

# menu.add("생선까스")  # 튜플은 수정 불가능 하므로 에러 발생

name = "KIM"
age = "20"
hobby = "reading"
print(name, age, hobby)  # KIM 20 reading

# 여러줄로 쓰는 대신 서로 다른 변수에 서로 다른 값들을 순서대로 넣어줌 (= 튜플)
(name, age, hobby) = ("LEE", 25, "dancing")
print(name, age, hobby)  # LEE 25 dancing

# 집합 (set)
# 중복 불가능, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3} (중복되는 값들은 무시)

# set 만드는 또 다른 방법: list[]로 만들고 set()으로 감싸줌
java = {"KIM", "LEE", "PARK"}
python = set(["KIM", "JUNG"])

# 교집합 출력
print(java & python)  # {'KIM'}
print(java.intersection(python))  # {'KIM'}

# 합집합 출력
print(java | python)  # {'JUNG', 'KIM', 'PARK', 'LEE'}
print(java.union(python))  # {'JUNG', 'KIM', 'PARK', 'LEE'}

# 차집합 출력
print(java - python)  # {'PARK', 'LEE'}
print(java.difference(python))  # {'PARK', 'LEE'}

# 집합에 value 추가
print(python)  # {'JUNG', 'KIM'}
python.add("PARK")
print(python)  # {'PARK', 'KIM', 'JUNG'}

# 집합에 value 삭제
print(java)  # {'KIM', 'LEE', 'PARK'}
java.remove("PARK")
print(java)  # {'KIM', 'LEE'}

# 자료구조의 변경
menu = {"coffee", "juice", "milk"}
print(menu, type(menu))  # <class 'set'>

menu = list(menu)
print(menu, type(menu))  # <class 'list'>

menu = tuple(menu)
print(menu, type(menu))  # <class 'tuple'>

menu = set(menu)
print(menu, type(menu))  # <class 'set'>

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample 활용
#
# 출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# -- 축하합니다 --
#
# 활용 예제)
# from random import  *
# list = [1, 2, 3, 4, 5]
# print(list)
# shuffle(list)  # list 안의 숫자 섞음
# print(list)
# print(sample(list, 1))  # 랜덤으로 숫자 뽑음


from random import *
users = range(1, 21)  # 1부터 20까지 숫자 생성
# print(type(users))
users = list(users)  # users의 type을 list로 바꿈
# print(type(users))

# print(users)
shuffle(users)  # users 안의 숫자들 섞음
# print(users)

winners = sample(users, 4)  # users에서 4명을 뽑음

print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))  # winners의 첫번째 숫자
print("커피 당첨자: {0}".format(winners[1:]))  # winners의 두번째~ 숫자
print("-- 축하합니다 --")
