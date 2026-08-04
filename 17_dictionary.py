# 리스트로 학생을 나열
data_class_list = ["학생1", "학생2", "학생3"]
# print(type(data_class_list)) <class 'list'>

# 딕셔너리 -> key와 value로 데이터를 저장 -> { key : value }
# 딕셔너리를 사용하기 위해서 key값을 숙지해야함

# 딕셔너리로 정확하게 역할 부여
data_class_dict = {
  "반장": "학생1", 
  "부반장": "학생2", 
  "당번": "학생3"
  }
# print(type(data_class_dict)) <class 'dict'>
# key와 value는 1:1 관계

# 센서로 부터 얻는 예시 데이터로 딕셔너리 만들기
sensors_dict = { "센서이름": "보일러",
                 "모터온도": 78,
                 "무쓸모": 100 }
# key값은 문자열을 쓰는 게 일반적

# 딕셔너리 key값으로 value값 가져오기
print(sensors_dict["센서이름"]) # 보일러

# 딕셔너리 value값 수정하기
sensors_dict["모터온도"] = 80

# 딕셔너리 수정 된 key값 프린트
print(sensors_dict["모터온도"]) # 80

# 딕셔너리 새 key값과 value값 추가
sensors_dict["진동"] = 0.5
# append 같은 함수를 쓰지 않고, 새로운 key값을 넣으면 value값이 추가됨

# 딕셔너리 key값으로 value값 삭제
del sensors_dict["무쓸모"]

# 딕셔너리 전체 프린트
print(sensors_dict) # {'센서이름': '보일러', '모터온도': 80, '진동': 0.5}

# 빈 딕셔너리 만들어서 나중에 데이터를 넣을 수도 있음
empty_dict = {} 
empty_dict["센서이름"] = "펌프"
empty_dict["모터온도"] = 80
empty_dict["진동"] = 0.5
print(empty_dict) # {'센서이름': '펌프', '모터온도': 80, '진동': 0.5}

# 딕셔너리로 잘못된 key값을 가져오면 error 발생
# error를 우려하여 .get("key값") 메서드를 사용하면 error를 방지할 수 있음
print(sensors_dict.get("모터온도")) # 80
print(sensors_dict.get("압력")) # None
motor_degree = sensors_dict.get("모터온도")

print(type(motor_degree)) # <class 'int'>
total_degree = motor_degree + 10
print(total_degree) # 90

# is_motor_degree_key = "모터온도" in sensors_dict
if "모터온도" not in sensors_dict:
  print("그런 키 없어요!")
else:
  print("그런 키 있어요!")

print("센서이름" in sensors_dict) # True
print("압력" in sensors_dict) # False
print("압력" not in sensors_dict) # True

# len()을 통해 몇 개의 key-value 쌍이 있는지 확인
print(len(sensors_dict)) # 3종류

if len(sensors_dict) < 5:
  print("내용이 부족합니다!")
else:
  print("내용이 충분합니다!")

# key값 value값 따로 가져오기
print(sensors_dict.keys()) # dict_keys(['센서이름', '모터온도', '진동'])
print(sensors_dict.values()) # dict_values(['보일러', 80, 0.5])

# .items() 메서드를 통해 key와 value를 list로 변환해서 동시에 가져오기
for key, value in sensors_dict.items():
  print(key, value)
# 센서이름 보일러
# 모터온도 80
# 진동 0.5
print(sensors_dict.items()) 
# dict_items([('센서이름', '보일러'), ('모터온도', 80), ('진동', 0.5)])

# 재미난 사례를 추가로 만들어보자
# 나라 이름
# 유럽 : 스페인(ESP), 프랑스(FRA), 독일(DEU), 스위스(SUI), 네덜란드(NLD)
# 아시아 : 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAU), 이란(IRN)
# 남미 : 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)
# 각 나라마다 이름과 약칭으로 정리 가능

korea = { "국가명": "대한민국", "약칭": "KOR" }
japan = { "국가명": "일본", "약칭": "JPN" }
asia_list = [korea, japan]
print(asia_list)
# [{'국가명': '대한민국', '약칭': 'KOR'}, {'국가명': '일본', '약칭': 'JPN'}]

# 포켓몬 1,2,3 진화단계들을 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 모인 배열을 만들어봅
# 그 배열 데이터를 확인해 print 합시
# (선택) 가능하면 그 배열 데이터 for-in 사용해 하나씩 꺼내 print 합시
# 다 되면 가만히 있기

pokemon_list =[ { "1단계": "파이리", "2단계": "리자드", "3단계": "리자몽" },
{ "1단계": "꼬북이", "2단계": "어니부기", "3단계": "거북왕" },
{ "1단계": "이상해씨", "2단계": "이상해풀", "3단계": "이상해꽃" },
{ "1단계": "캐터피", "2단계": "단데기", "3단계": "버터플" },
{ "1단계": "구구", "2단계": "피죤", "3단계": "피죤투" },
{ "1단계": "또가스", "2단계": "또도가스", "3단계": "또또도가스" },
{ "1단계": "미뇽", "2단계": "신뇽", "3단계": "망나뇽" },
{ "1단계": "피존", "2단계": "피죤투", "3단계": "피죤투2" },
{ "1단계": "꼬렛", "2단계": "레트라", "3단계": "레트라2" },
{ "1단계": "물짱이", "2단계": "슈륙챙이", "3단계": "강챙이" } ]

for pok in pokemon_list:
#  print(f"1단계: {pok.get("1단계")}, 2단계: {pok.get("2단계")}, 3단계: {pok.get("3단계")}")
#  print(pok)
  for key, value in pok.items():
    print(f"{key}: {value}")

print("===========================================")

# 두 딕셔너리 key-value 조합으로 하나씩 꺼내어 비교하기
# 다음 두 딕셔너리는 같은 key들을 가지고 있는 게 전제
# 실제 데이터
values = {"모터온도": 95, "압력": 88 }
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90 }

for name, value in values.items():
  if value > limits.get(name, 0): # limits 라는 딕셔너리의 name이라는 key값을 넣어 비교
    print(name, "경고")

sensors = { "모터온도": 78, "진동": 0.5 }
new_data = { "모터온도": 80, "유량": 42 }
sensors.update(new_data)
print(sensors) # {'모터온도': 80, '진동': 0.5, '유량': 42}

# zip으로 key들의 배열과 value들의 배열을 묶어서 새로운 딕셔너리를 만들 수 있음
names = ["모터온도", "진동", "압력"]
values = [ 78, 0.5, 95 ]
sensors = dict(zip(names,values)) # {'모터온도': 80, '진동': 0.5, '유량': 42}

# 딕셔너리 만들기 전 설계
# 1. key값과 value값 정하기
# 2. 원하는 값을 쉽게 찾는 구조
# 2-1. 이 결과를 위해서
#      리스트 안에 딕셔너리 구조가 좋겠다 
#   or 딕셔너리 안 리스트 구조가 좋겠다

plant = [
  {
  "1번모터": {"온도": 78, "상태": "정상"},
  "2번펌프": {"압력": 78, "상태": "경고"},
},
{
  "1번모터": {"온도": 78, "상태": "정상"},
  "2번펌프": {"압력": 99, "상태": "몰루"},
}
]
print(plant[1]["2번펌프"]["상태"])

# 딕셔너리 안에 value로 딕셔너리를 사용하기
kbo = [
  {
    "구단명": "삼성",
    "마스코트": "라이온스",
    "구장": [
      "대구라이온스파크",
      "포항야구장"
    ]
  },
  {
      "구단명": "두산",
      "마스코트": "베어스",
      "구장": {
        "1구장": "잠실야구장",
        "2구장": "베어스파크"
      }
    },
]
# 쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근하기
print(kbo[0]["구장"][1]) # 포항야구장