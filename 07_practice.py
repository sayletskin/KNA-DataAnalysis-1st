# 실습39
# name = input("이름: ")
# print(f"(안녕하세요 {name}님!)") # (안녕하세요 김정렬님!)

# 실습40
# year = int(input("태어난 해: "))
# age = 2026 - year + 1
# print(age)

# 실습41
# city = input("도시: ")
# country = input("나라: ")
# print(country + "의 " + city + "에서 거주하시는군요!")

# 실습42
# a = int(input("수1: "))
# b = int(input("수2: "))
# print(a + b, a - b, a * b, a / b)

# 실습43
# 출력 결과 1 : 80 초과 , 출력 결과 2 : 0 이상
# bool형으로 출력
# temp = float(input("온도: ")) # 임의 온도 24.5
# print("80도 초과", temp > 80) # 80도 초과 False
# print("0도 이상", temp >= 0) # 0도 이상 True

# 실습44
a = int(input("A점수: ")) # 점수는 정수라 가정
b = int(input("B점수: "))
c = int(input("C점수: "))
avg = (a + b + c) / 3
print(avg, avg >= 60)
# A점수: 60
# B점수: 50
# C점수: 80
# 63.333333333333336 True

