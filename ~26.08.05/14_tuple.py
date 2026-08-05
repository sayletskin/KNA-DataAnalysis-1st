# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,(콤마)를 붙여야 Python이 튜플로 인식
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = ()  # 괄호 있고, 끝에 쉼표 없고, 값도 안담김
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 튜플
# 요소 1개: 쉼표 여부
# 요소 0개(빈 튜플): () 빈 괄호

# 튜플에서 헷갈리는 것
# (1) : int
# (1,) : tuple

# (1, 2, 3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# (1, 2, 3) : tuple

# 튜플의 인덱스
# 인덱스로 요소값 가져오기
sensor = ("모터온도", 78,)
print(sensor[0]) # 모터온도

# 튜플의 슬라이싱
s = ('a', 'b', "c", "d", "e",)
print(s[1:4]) # ('b', 'c', 'd')
# 슬라이싱 한 결과는 소괄호에 감싸져 있음
# 튜플은 슬라이싱해도 튜플

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언
a, b, c = "a", "b", "c"

unpacking = (1, 2, 3,) # 각각 변수 one, two, three 에 담아봄
## unpacking = one, two, three
# one, two, three라는 알 수 없는 변수를
# unpacking 변쉐 할당하겠다는 의미
# 동작x

one, two, three = unpacking
# unpacking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에
# 풀어서 담는다는 뜻
print("one", one) 
print("two", two)
print("three", three)

# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까?
one, two, three, four = [11, 22, 33, 44]
print("one", one) 
print("two", two)
print("three", three)
print("four", four)
# 가능

# =========================================

tup = ("normal", "normal", "warning", "normal", "warning",)

# 튜플의 길이
print(len(tup)) # 5

# 튜플의 특정값 갯수 세기
print(tup.count("warning")) # 2
print(tup.count("WarNing")) # 0

# 튜플의 특정값 처음 나온 인덱스
print(tup.index("warning")) # 2
# print(tup.index("WarNing")) # error

# tuple list
# list 안에 복수의 tuple을 담는 것을 표현
# list를 사용해서 list 내부의 tuple에 접근하고
# tuple에 담긴 값을 사용할 수 있음

# unpacking을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

hour_13 = [("모터온도", 77), ("모터진동", 0.2), ("모터압력", 91),]
now = 0

for name, value in hour_13:
  now += 1
  print(f"{now}번째 반복")
  print("name:", name, "value:", value)
  
# =================================

temps_13 = [ ("qox_001", 81), ("qox_002", 88), ("qox_003", 95), ("qox_004", 89),]
warning = 90
# 90 도 이상이면 경고 출력
for name, temp in temps_13:
  if temp >= warning:
    print("경고", name, "설비 온도 이상")

# list 안에 튜플 갯수가 늘어나면 for문에서 변수를 여러 개 작성

tup_list = [("일", "one", 1, "1"), ("이", "two", 2, "2"),]
print(len(tup_list)) # 2 리스트 요소 수
print(len(tup_list[0])) # 4 리스트 안 0번 째 튜플 요소 수

for kor_str, eng_str, num, num_str in tup_list:
  print(kor_str, eng_str, num, num_str)

# ================================

# 튜플 리스트 정렬
# sorted()를 사용하여 튜플의 특정 값 기준으로 리스트를 정렬
temps_13 = [ (81, "qox_001"), (88, "qox_002"), (95, "qox_003"), (89, "qox_004"),]

hot = sorted(temps_13, reverse=True)
print(hot)

# 실습 1
tup = ("센서1", 77)
print(tup) # ('센서1', 77)
print(tup[0]) # 센서1
print(tup[1]) # 77
name, temp = tup
print(name, temp) # 센서1 77

# 실습 2
lists = [("센서1", 87), ("센서2", 91), ("센서3", 89), ("센서4", 93),]

for name, temp in lists:
  if temp > 90:
    print(name, "경고") # 센서2 경고, 센서4 경고

print("===================")    
#실습 3
lists = [("센서1", 87, (5, 3)), ("센서2", 91, (2, 4)), ("센서3", 89, (7, 5)),]

for name, temp, pos in lists:
  x, y = pos
  print(name, "위치:", x, y)
print("===================")   
for name, temp, pos in lists:
  x, y = pos
  if x <= 5:
    print(name, temp, "펌프압력?")
