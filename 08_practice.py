# 실습 45
name = "PUMP_A"
stat = "정상"
run_h = 1200
day = "2026-07-16"
# 내가 쓴거
print("설비:", name, "\n상태:", stat, "\n가동:", run_h, "\n점검:", day)
# 리더가 쓴거
card = "설비: " + name + "\n상태: " + stat + "\n가동: " + str(run_h) + "\n점검: " + day
print(card)
# 쉼표는 독립된 개체로 인식해서 + 쓰는 것을 권장

# 실습 46, 47
word = "temp_sensor"
print(word[:4]) # temp
print(word[5:]) # sensor
print(word[3:6]) # p_s

# 실습 48
word = "sensor_01"
print(word[-2:]) # 01

# 실습 49, 50
word = "PYTHON"
print(word[::2]) # PTO
print(word[::-1]) # NOHTYP

# 실습 51
num = "01012345678"
print(len(num)) # 11

# 실습 52
word = "a,b,c,d"
print(word.count(",")) # 3

# 실습 53 (안함)
word = "a,b,c,d"
print(word.find(",")) # 1

email = "qkqhro52@naver.com"


# 1주차 복습
# len() 문자열 숫자 세줌
line = "=" * 20
print(line)
print(len(line))

# in 특정 단어가 들어가있으면 True False
print("@" in email)
print("google" in email)
print("@" not in email)
print("google" not in email) 

# count() 개수 세기 / 문자열에 사용하는 함수여서 온점(.)을 사용
print("a-b-b-c-d-a".count("-"))
print(email.count("q"))

# find() 특정 글자가 처음 나오는 위치 찾아줌 / 얘도 문자열 뒤에 . 사용
print(email[:email.find("@")])
at = email.find("@")
print(email[:at]) # 상황마다 다름, 계속 사용할거면 at으로 변수할당 하는게 맞고, 한번만 할거면 그냥 집어넣기

# index() 위치 찾기 , find 파트너 / 차이점 email에 "@"를 대입하면 둘 다 4 라는 결과가 나오지만, "-"를 대입하면 find는 -1 index는 오류

# startswith 특정 단오로 시작하는지 참.거짓 / endswith 특정 단어로 끝나는지 참.거짓 (bool형)
# in 은 어디든지 들어있으면 True 지만 위 두 명령은 위치에 따라 들어있어도 False가 될 수 있음

# 실습 53
name = "sensor_log.csv"
print(name.startswith("sensor")) # True
print(name.endswith(".csv")) # True

# 실습 54
str1 = "ready"
str1_upper = str1.upper()
print(str1_upper)

# 실습 55
str2 = "WARNING"
s_lower = str2.lower()
print(s_lower) # warning

# 실습 56
print("ABC".isupper()) # True
print("abc".islower()) # True
print("Abc".isupper()) # False

# 실습 57
name = "Sensor_LOG.CSV"
low = name.lower()
print(low.startswith("sensor")) # True
print(low.endswith(".csv")) # True

# 실습 58
str3 = "     Warning     "
str3_low = str3.lower()
print("[" + str3_low + "]") # [     warning     ]
str3_chain = str3.lower().strip()
print("[" + str3_chain + "]") # [warning]

day = "2026-07-27"
print(day.split("-"))

# 실습 59
text = "a,b,c,d"
print(text.split(",")) # ['a', 'b', 'c', 'd']

text_list = text.split(",")
print(text_list[2]) # c 

# 실습 60
date = ['2026','07','27']
print("-".join(date)) # 2026-07-27

# 실습 > 변수에 "python"이라는 문자열 할당
# "phThon" 이라고 출력
s = "python"
print(s.replace("t","T")) # pyThon

# 실습 62
date = "2026/07/27"
date_spl = date.split("/")
print("-".join(date_spl)) # 2026-07-27
print("-".join(date.split("/"))) # 2026-07-27

# 실습
s = "1, NORMAL ,25.3"
s_spl = s.split(",") # ['1', ' NORMAL ', '25.3']
s_cha = s_spl[1].strip().lower()
print(s_cha) # normal

name = "kjr"
age = "25"
print(f"저는 {name}이고, {age}살 입니다")

# 실습
name, temp = "PUMP_A", 87
print(f"설비 {name}, 온도 {temp}도") # 설비 PUMP_A, 온도 87도 
print("설비 " + name + ", 온도 " + str(temp) + "도") # 설비 PUMP_A, 온도 87도

# 실습
a, b, c = 17, 25, 43
print(f"평균 {(a + b + c) / 3:.2f}") # 평균 28.33 
# f-string 안에 .:2f 쓰면 소수점 2번째 자리 반올림

# 실습
num = 87.456
print(f"측정값 {num:.2f}") # 측정값 87.46
print(f"측정값 {num:.1f}") # 측정값 87.5

# 실습
str4 = " 5 , sensor_2 , WARNING , 0.78912 "
str4_1 = str4.strip().split(",")
sens = str4_1[1].strip()
stat = str4_1[2].strip().lower()
num = float(str4_1[3].strip()) 
# 공백 때문에 str 판정이 되서 float으로 바꿔야 하는듯 (X)
# 애초에 str4 가 "따옴표"로 감싸져서 그냥 str판정이다 (O)
print(f"[센서 {sens}] 상태 {stat}, 측정값 {num:.2f}")
# [센서 sensor_2] 상태 warning, 측정값 0.79

# 복습
str5 = ("안녕", "하세요", "여러분", "저는", "홍길동", "입니다")
print(str5, sep='d') 
print("안녕", "하세요", "여러분", "저는", "홍길동", "입니다", sep='d', end='!\n')
a, b, c = ("하세요", "저는", "입니다")
print(f"안녕{a}.\n\n여러분 {b}\n홍길동{c}.")

d, e = ( 0.123 ), " 0.123 "
print(f"소수 확인: {d}")
print(f"소수 확인: {e}")
print(f"소수 확인: {d:.2f}")
e_1 = float(e)
print(f"소수 확인: {e_1:.2f}")

str6 = "안녕 하세요 여러분 저는 홍길동 입니다"
str6_spl = str6.split()
print(str6_spl)
str6_join = "^".join(str6_spl)
print(str6_join)


