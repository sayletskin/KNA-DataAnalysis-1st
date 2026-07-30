temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []


for t in temps:
  doubled.append(t * 3)

print(doubled) # 기존 temps 모든 요소에 3을 곱한 리스트

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
high = []
low = []

for t in temps:
  if t < 5:
    low.append(t)
  else:
    high.append(t)

# 복습) .sort() > 원본 배열을 오름차순 
# but 반환X 따라서 print 바로 찍으면 None 출력
low.sort(), high.sort()
print(low, high) # temps 에서 5보다 작은 요소를 low에 그 외는 high

# 리스트 안의 리스트
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 인덱스 리스트를 "열"

print(rows[0]) # ['펌프', 25]
print(type(rows[0])) # <class 'list'>
# 중첩된 리스트 안에 접근하고 싶을 때
print(rows[1][1]) # 32
# 1. rows[1]을 찾음 -> ["모터", 32]
# 2. print(["모터", 32][1]) -> 1번 값의 [1]
# 3. print(32) -> 32 출력
# 중첩된 리스트 내부의 값은 대괄호를 여러번 이어서 접근

# 리스트 안의 리스트 온도값만 출력하기
for row in rows:
  print(row[0], "온도", row[1]) # 펌프 온도 25, 모터 온도 32, ...
# rows는 리스트를 담고 있는 큰 리스트
# row는 rows 안에 있는 작은 리스트
