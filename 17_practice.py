# 실습 1. 딕셔너리 만들고 다루기

# 1) 센서명을 key 측정값을 value 으로 딕셔너리 저장
sensors = {
  "모터온도": 78,
  "진동" : 0.5,
}

# 2) key로 value를 꺼내고 새 key로 추가, 기존 key 수정
print(sensors["진동"]) # 값 꺼내기
print(sensors.get("진동", 0)) # 값 안전하게 꺼내기

sensors["압력"] = 95 # key, value 추가
sensors["진동"] = 0.3 # value 수정

print(sensors)

# 3) get으로 없는 key를 기본값으로 조회, in으로 확인
print(sensors.get("면적", -1)) # 면적은 존재하지 않아서 -1로 대체
print("진동" in sensors) # True
print("면적" in sensors) # False



# 실습 2. update로 여러 값 한 번에 갱신하기

# 1) 센서 딕셔너리와 새 데이터 딕셔너리 저장
sensors = { "모터온도": 78, "진동": 0.5 }
new_data = { "모터온도": 80, "유량": 42 }

# 2) update로 새 데이터를 반영
sensors.update(new_data)

# 3) del키로 삭제하고 len 개수 확인
del sensors["모터온도"]
print(len(sensors)) # 2




# 실습 5. 임계값으로 경고 센서 분류하기

# 1) 측정값 딕셔너리, 임계값 딕셔너리 저장
# 측정값 데이터
values = {"모터온도": 95, "압력": 88 }
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90 }

empty = []
# 2) items 로 순회해서 각 값이 임계값 넘는지 비교
for name, value in values.items():
  if value > limits[name]:
# 3) 넘는 센서 빈 리스트에 모아 출력
    empty.append(name)
print("경고:", empty) # ['모터온도']




# 실습 6. 

# 1) 설비명을 key, 설비정보를 딕셔너리를 값으로 하는 딕셔너리 저장
plant =  {
  "1번모터": {"온도": 78, "상태": "정상"},
  "2번펌프": {"압력": 80, "상태": "경고"},
}

# 2) 중첩 키로 특정 설비 특정 값 꺼내기
# 2번펌프 압력값
print(plant["2번펌프"]["압력"]) # 80

# 3) items 순회로 "경고" 설비 찾아 출력
for num, dict in plant.items():
  for name, value in dict.items():
    if value == "경고":
      print(num)

print("===========================")

# 간단하게 딕셔너리 예재를 만들어봅시다
# 지역에 대한 구분
location_dict = {
  "시": [
    {
      "이름": "서울특별시",
      "기초단체": [ "종로구", "중구", "마포구" ]
    },
    {
      "이름": "대구광역시",
      "기초단체": [ "중구", "수성구", "달서구" ]
    }
  ],
  "도": [
    {
      "이름": "경기도",
      "기초단체": [ "수원시", "안양시", "안산시" ]
    },
    {
      "이름": "경상북도",
      "기초단체": [ "포항시", "경주시", "인천시" ]
    }
  ]
}
print(location_dict)
print("============================")

# 시와 도 단위 딕셔너리들을 각각 출력하기
print(location_dict.get("시", 0))
print(location_dict.get("도", 0))
print("============================")

# 각 시 도 마다 세부 딕셔너리드를 출력하기
for basic_dict in location_dict["시"]:
  print(basic_dict.get("이름"))
  print(basic_dict.get("기초단체"))
  print("============================")

for basic_dict in location_dict["도"]:
  print(basic_dict.get("이름"))
  print(basic_dict.get("기초단체"))
  print("============================")

# 위 코드를 보면 두 개의 for문이 사실상 같은 일을한다
# 그래서 중복되는 부분을 묶고,
# 다른점만 외부에서 지적해 시키면 들어가는
# "함수(function)"를 만들면 효율성이 높아진다