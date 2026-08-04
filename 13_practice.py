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
    blank.append(round(t * 1.8 + 32, 2))
print("30도 넘는 온도의 화씨:", blank)
# 30도 넘는 온도의 화씨: [87.8, 98.6]

# 실습
temps = [25, 35, 31, 28, 32, 26]
total = 0
blank = []

for t in temps:
  total += t
print(total / len(temps)) # 177 / 6 = 29.5 전체 평균

for t in temps:
  if t > 30:
    blank.append(t)

blank_total = 0
for b in blank:
  blank_total += b
print(len(blank)) # 3 고온 개수
print(round(blank_total / len(blank), 1)) # 32.7 고온 평균

