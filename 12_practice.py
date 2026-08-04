answer = 11
guess = 0

while answer != guess:
  guess = int(input("숫자(1~50): "))
  if guess < 11:
    print("up")
  elif guess > 11:
    print("down")
print("정답")

found = False
n = int(input("반복횟수: "))

for i in range(n):
  v = int(input("측정값: "))
  if v >= 2:
    found = True
    break

if found:
  print("발견")
else:
  print("없음")

print("==============구분선=============")

total = 0
found = False

for i in [4, 7, 6]:
  if i > 11:
    found = True

if found:
  print("있음")
else:
  print("미발견")

print("==============구분선=============")

# 최댓값 찾기

first = int(input("1번째 값: "))
max_num = first

for i in range(2):
  v = int(input(f"{i + 2}번째 값: "))
  if v > max_num:
    max_num = v
print("최댓값:", max_num)

# 최솟값 복습

first = int(input("첫번째 값: "))
min_num = first

for i in range(2):
  v = int(input(f"{i + 2}번째 값: "))
  if v < min_num:
    min_num = v
print("최솟값:", min_num)

# 조건을 걸어 누적된 수의 합을 구함
# 결과는 누적의 합과 누적된 수가 몇 개인지도

count = 0
total = 0

for i in [11, 22, 33, 44, 55]:
  if i % 2 == 0:
    count += 1
    total += i
print("갯수:", count, "합계:", total)

while True:
  i = input("숫자1 넣으면 종료: ")
  if i == "1":
    print("종료")
    break
  print("너가 입력한 문자: ", i)

# 실습
temps = [27, 31, 28, 30, 21, 37]
temps.sort()

for i in temps:
  if i >= 30:
    print("고온:", i)

# 실습
hours = [3, 6, 4, 7, 2, 5, 10]

for h in hours:
  if h >= 5 and h <= 10:
    print(h)

# 실습
temps = [27, 31, 28, 30, 21, 37]
total, count = 0, 0

for t in temps:
  if t > 30:
    total += t
    count += 1
print("평균:", total / count) # total 68 count 2 평균 34.0

# 실습
temps = [27, 31, 28, 30, 21, 37]
blank = []

for t in temps:
  if t > 30:
    blank.append(t)
print("30초과 온도:", blank, "30초과 온도 개수:", len(blank))
# 30초과 온도: [31, 37] 30초과 온도 개수: 2

# 실습
temps = [27, 31, 28, 30, 21, 37]
blank = []

for t in temps:
  if t > 30:
    blank.append(t * 1.8 + 32)
print("30도 넘는 온도의 화씨:", round(blank))