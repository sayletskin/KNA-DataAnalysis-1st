# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5) # 8
print(10 - 4) # 6
print(4 * 5) # 20
print(40 / 8) # 5.0 나눗셈 결과는 항상 float
print(11 // 3) # 3 몫
print(11 % 3) # 2 나머지
print(2 ** 10) # 1024 2의 10제곱

# ==========================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱) > *(곱하기) /(나누기) //(몫) %(나머지) > +(더하기) -(빼기)

print(3 +5 * 4) # 5 * 4 먼저 계산 후 3을 더함
print((3 + 5) * 4) # 괄호 안의 연산을 먼저한 뒤 곱하기 계산

# ==========================
# 복합 연산자

result = 3 * 5
print(result) # 15
# +=: 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -=: 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# *=: 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /=: 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10 # 25
result -= 5 # 20
result *= 3 # 60
result /= 2 # 30.0 float 조심하자
print(result)

# ======================
# 문자열 연산
print("안녕" + "하세요") # 안녕하세요

# 만약 "안녕"과 "하세요" 사이에 공백을 1개 넣고싶다면
# 방법 1) , 사용
print("안녕", "하세요")
# 방법 2) 안녕 뒤에 공백 추가
print("안녕 " + "하세요")
# 방법 3) 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5) # 안녕안녕안녕안녕안녕

# 문자열을 연산자를 사용할 경우 모두 이어져서 나옴

# 실습32
a = 17
b = 5
print(a + b) # 22
print(a - b) # 12
print(a * b) # 85
print(a / b) # 3.4
print(a // b) # 3
print(a % b) # 2
print(a ** b) # 1419857

# 실습33
a, b, c = 4, 6, 9 # 평균
d = 11 # 정사각형 한 변의 길이
x, y, z = 2, 5, 9 # 직육면체 가로, 세로, 높이
print((a + b + c) / 3) # 6.3333
print(d ** 2) # 121
print(x * y * z) # 90

# 실습34
a, b = "안녕", "안녕"
print(3 == 3) # True
print(3 != 3) # False
print(3 > 3) # False
print(3 < 3) # False
print(a >= b) # True , str끼리도 같으면 >=에서 True가 뜸
print(3 <= 3) # True

# 실습35
temp = 85
temp_ok = 60 <= temp and 90 >= temp
pressure = 5
pres_ok = pressure >= 3 and pressure <=7
print(temp_ok) # True
print(pres_ok) # True
print(pres_ok and temp_ok) # True and True = True

# 실습36
stock = 100
stock += 50 # 150
stock -= 30 # 120
stock += 5 # 125
print(stock) # 125

# 실습37
total, defect = 500, 23
run_h, all_h = 21, 24
print(defect / total * 100, run_h / all_h * 100)
# 불량률 4.6%, # 가동률 87.5%

# 실습38
run_t = 500
run_h = run_t // 60
run_m = run_t % 60
print(run_h, "시간", run_m, "분") # 8 시간 20 분 
print(f"{run_h}시간 {run_m}분") # 8시간 20분