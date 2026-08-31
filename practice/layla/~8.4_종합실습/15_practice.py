# 실습 4
sens_a = ["NOK_01", "NOK_01", "NOK_03", "NOK_03", "NOK_04", 
          "NOK_04", "NOK_06", "NOK_06", "NOK_01", "NOK_03"]
sens_a_sort = sorted(set(sens_a))
print("sort:", sens_a_sort, "len:", len(sens_a_sort))
# sort: ['NOK_01', 'NOK_03', 'NOK_04', 'NOK_06'] len: 4

# 실습 1
temps = [31, 25, 43, 23]

for t in temps:
  if t >= 30:
    print("고온:", t) # 고온: 31, 고온: 43

# 실습 2
hours = [3, 9, 5, 7]

for h in hours:
  if h >= 5 and h <= 10:
    print("(5~10):", h) # (5~10): 9, (5~10): 5, (5~10): 7

# 실습 3
NOK_temps = [27, 29, 31, 33]
NOK_total = 0
NOK_count = 0

for t in NOK_temps:
  if t > 30:
    NOK_total += t
    NOK_count += 1
print("30 초과 온도:", t)
print("30 초과 온도 합:", NOK_total)
print("30 초과 온도 갯수:", NOK_count)
print("30 초과 온도 평균:", NOK_total / NOK_count)