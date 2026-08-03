# set

# 자동 중복 제거
# 순서가 없음
# 형태는 중괄호로 감쌈

# 빈 set 만들기
list_ = [] # 빈 리스트
tuple_ = () # 빈 튜플
print(type(list_), type(tuple_))

empty_set = {}
print(type(empty_set)) # <class 'dict'>
# 빈 중괄호는 dictionaly라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장함수를 사용
real_empty_set = set()
print(type(real_empty_set)) # <class 'set'>

# 값을 포함한 셋 만들기
logs = ["S01", "S02", "S01", "S03", "S01"]

# 리스트를 {}에 감쌀 경우
## unique = {log} # 에러

# 복수의 값을 중괄호에 감싸 작성
unique = {"S01", "S02", "S01", "S03", "S01"}
print(unique) # {'S01', 'S02', 'S03'}
print("==================")
# set() 사용
unique = set(logs)
print(type(unique)) # <class 'set'>
print(unique) # {'S02', 'S01', 'S03'}
# unique 셋에는 기존 중복되었던 S01이 한 번만 들어감
# 지그믄 길이가 짧아서 순서대로 정렬된 것 처럼 보이지만 (나는 정렬 안됨)
# 셋은 "순서가 없는 값의 묶음"

## print(unique[0]) # TypeError: 'set' object is not subscriptable
# set에서 인덱스 사용시 에러

# set에 바로 여러 값을 작성
unique = set(["S01", "S02", "S01", "S03", "S01"])
print(unique)

# set을 사용해서 리스트에 들어있는 값의 종류 수를 알 수 있음
print(len(unique)) # 중복되지 않는 값 3

# =================

# 셋에 값 추가하기
# 셋.add (추가할 값)
# 이미 있는 값을 추가할 경우 무시

# alerts (경보가 있는 센서)
alerts = {"S01", "S02"}

# 경고 상태인 S03이 추가될 경우
# .add()를 사용해서 추가
alerts.add("S03")
print(alerts) # {'S01', 'S03', 'S02'}

# S01에서 또 경고가 발생
# 이미 S01은 경고가 발생한 적이 있고
# alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관 없이
# 이럴 때 set을 쓰면 편함
alerts.add("S01")
print(alerts) # {'S01', 'S02', 'S03'}
# S01이라는 값을 또 추가해도 무시하고 한 번만 지정
# 그래서 독립적인 값을 저장하기에는 아주 편리함

# set을 정렬(sorted)하면?
sorted_set = sorted(alerts) # sorted 에 마우스 올리면 list로 반환한다고 적힘
print(sorted_set) # ['S01', 'S02', 'S03']
# 그래도 중복없이 정렬해서 리스트하기 좋네

# alerts. 내장 메서드가 list 보단 적어서 메모리가 비교적 가볍

#======================
# set에 특정 값 포함 여부 확인
# ["S01", "S02", "S01", "S03", "S01"]
# {'S01', 'S03', 'S02'}
# list와 set을 비교하면
# set이 길이가 짧음 (중복 제거 때문)
# set은 인덱스가 없음 (순서X)
# 순회 속도가 리스트보다 훨씬 빠름

print("S01" in alerts) # True
# 이렇게 출력하기보단 조건문을 활용해서
# 포함 여부 확인 후 특정 동작을 실행시킴
if "S01" in alerts:
  print("S01 정비 필요")

# 실습 4
sens = ["WOR_01", "WOR_01", "WOR_01", "WOR_01",
         "WOR_06", "WOR_06", "WOR_03", "WOR_05"]
sor_set_sens = sorted(set(sens))
print(sor_set_sens) # ['WOR_01', 'WOR_03', 'WOR_05', 'WOR_06']
print(len(sor_set_sens)) # 4

# ==============================

# 집합 연산
hour_14 = {"WOR_01", "WOR_06", "WOR_07", "WOR_02"}
hour_15 = {"WOR_01", "WOR_07", "WOR_03", "WOR_09", "WOR_011"}

# 합집합 union | 
print(hour_14.union(hour_15))
print(hour_14 | hour_15)
# {'WOR_01', 'WOR_09', 'WOR_011',
#  'WOR_06', 'WOR_02', 'WOR_03', 'WOR_07'}
print(hour_14) # {'WOR_01', 'WOR_02', 'WOR_06', 'WOR_07'}
# .union은 원본 셋에 변화X
# hour_14와 hour_15 순서를 바꿔도 같다

# 교집합 intersection &
# union이랑 동일하게 두 코드는 똑같은 결과를 출력
# 앞뒤 순서가 결과에 영향을 미치지 않음
print(hour_14.intersection(hour_15))
print(hour_15.intersection(hour_14))
print(hour_15 & hour_14) # 모두 {'WOR_01', 'WOR_07'}

# 차집합 difference -
# 순서에 따라 결과가 다름
# 앞에 작성된 셋에서 difference의 인자로 전달된 셋에
# 있는 값들을 제외한 결과를 출력
print(hour_14.difference(hour_15)) # {'WOR_02', 'WOR_06'}
print(hour_14 - hour_15) # {'WOR_02', 'WOR_06'}
print(hour_15.difference(hour_14)) # {'WOR_011', 'WOR_09', 'WOR_03'}
# 차집합은 순서에 따라 결과가 다른 것 유의

# 실습 5
line_1 = {"NOK_1", "NOK_2", "NOK_3", "NOK_4"}
line_2 = {"NOK_0", "NOK_2", "NOK_4", "NOK_6"}
print(line_1.union(line_2))
# {'NOK_3', 'NOK_4', 'NOK_6', 'NOK_0', 'NOK_2', 'NOK_1'}
print(line_1.intersection(line_2)) # {'NOK_2', 'NOK_4'}
print(line_1.difference(line_2)) # {'NOK_3', 'NOK_1'}
print(line_2.difference(line_1)) # {'NOK_0', 'NOK_6'}

# 실습 6
to_d = {"NOK_1", "NOK_2", "NOK_3", "NOK_4"}
yester_d = {"NOK_0", "NOK_2", "NOK_4", "NOK_6"}
# 오늘만 있는 신규 이상 센서
print("신규:", to_d.difference(yester_d))
# 신규: {'NOK_3', 'NOK_1'}
# 어제, 오늘 지속된 이상 센서
print("지속:", to_d.intersection(yester_d))
# 지속: {'NOK_4', 'NOK_2'}