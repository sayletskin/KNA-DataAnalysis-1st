# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
temp = 36 # 숫자 따옴표 x
name = "센서A" # 글자 변수 지정은 무조건 따옴표

print(temp) # 36
print("temp") # temp
# = 은 "같다"가 아니라 "저장"하는 것
# 비교는 ==을 사용

# =========================
print("===== qustn tkdyd ghkfdydd =====")

x = 5
x = x + 5 
# 변수를 "재할당"할 때 변수 기존 자신의 값을 활용할 수 있음
# 변수를 할당할 때 오른쪽을 먼저 계산한 뒤 x에 값을 재할당 (=는 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드)
print(x) # 10

# y = y + 5 # 오류발생, y = y + 5 는 y가 선언되지 않았기 때문

# ================
print("====재할당======")

print("재할당하기 전 temp:", temp)
temp = 15 # 위에서 할당했던 36이라는 값을 15로 재할당
Temp = 150 # temp와 다른 변수로 동작
print("temp:", temp, "Temp:", Temp)

# 재할당은 가장 마지막으로 실행된 코드 값이 불려옴
score = 100
print(score) # 100
score = 90
score = 30
print(score) # 30

# ===========================
print("========= 값 복사 ============")
a = 10
b = 10 # b 변수에는 10이 저장 (저장할 때의 그 순간의 a값을 b에 복사)
a = 100 # a 변수를 재할당해도 
print(b) # b 변수의 값은 10 그대로 유지됨

# ===========================
print("===== 여러 변수 한 번에 선언 및 할당 =========")

width, height = 10, 20 # width = 10, height = 20 이 할당
# 주의 사항: 변수1, 변수2, ... = 값1, 값2, ... <변수와 값 갯수가 같아야 함
# x, y , z = 10, 20 # 변수 3개, 값 2개 >> ValueError 발생
print("width:", width, "height:", height)

# ===========================
print("===== 주석으로 변수 설명 =======")

temp = 25 # 온도(섭씨) [temp_상세정보]
count = 3 # 센서 개수
# temp = 100123456 # 주석처리된 코드는 동작x
print(temp)

# 실습1
temperature = 30
print(temperature) # 30
name = "센서A"
print(name) # 센서A

# 실습3
my_number = 5
print(my_number) # 5
mood = "평온"
print(mood) # 평온

# 실습4
age = 29
label = "나이"
print(label) # 나이
print(age) # 29

# 실습15
x = 10
print(x) # 10
x = x + 5
print(x) # 15
x = x * 2
print(x) # 30

# 실습16
a = 100
b = a
a = 999
print(a, b) 
# a=999, b=100 a값(100)이 b에 저장되었고 a값만 바뀌고(999) b는 그대로(100)이다.

# 실습17
