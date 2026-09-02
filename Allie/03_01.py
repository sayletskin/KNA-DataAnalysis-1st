import pandas as pd

tags = pd.read_csv('data/03-01_회전기계_신호_회전기계태그목록.csv')
df = pd.read_csv('data/03-01_회전기계_신호_진동추세.csv')

# 1번 모터에 대한 태그 목록
# ["tag", "indicator", "summary", "unit", "direction"]
print(tags.loc[tags["equipment"] == "1번 모터", ["tag", "indicator", "summary", "unit", "direction"]])
# 0    MTR01_VIB_H        속도     RMS  mm/s        수평
# 1    MTR01_VIB_V        속도     RMS  mm/s        수직
# 2    MTR01_VIB_A        속도     RMS  mm/s       축방향
# 3  MTR01_VIB_ACC       가속도    PEAK     g        수평
# 4  MTR01_CURRENT        전류     순시값     A      해당없음
# 5     MTR01_TEMP        온도     순시값  degC      해당없음
# 6      MTR01_RPM       회전수     순시값   rpm      해당없음

# 진동의 정상 범위 정하기
# 맨 앞 기준으로 20일 구간을 정상 기간으로 볼 것
MTR = ["MTR01_VIB_H", "MTR01_VIB_V", "MTR01_VIB_A", "MTR01_VIB_ACC"]
normal = df.head(20)

print(normal[MTR].agg(["max", "min"])) # 극단값 (최대, 최소값) 출력
#      MTR01_VIB_H  MTR01_VIB_V  MTR01_VIB_A  MTR01_VIB_ACC
# max          2.1          1.6          0.8           0.56
# min          1.7          1.3          0.7           0.51

## 펌프 극단값 출력해보기
print(tags.loc[tags["equipment"] == "1번 펌프", "tag"])
# 7         PMP01_VIB_H
# 8         PMP01_VIB_V
# 9         PMP01_VIB_A
# 10      PMP01_VIB_ACC
# 11      PMP01_CURRENT
# 12    PMP01_PRESS_SUC
# 13         PMP01_FLOW

PMP = ["PMP01_VIB_H", "PMP01_VIB_V", "PMP01_VIB_A", "PMP01_VIB_ACC"]
print(normal[PMP].agg(["max", "min"]))
#      PMP01_VIB_H  PMP01_VIB_V  PMP01_VIB_A  PMP01_VIB_ACC
# max          2.2          1.7          1.0           0.63
# min          2.0          1.6          0.9           0.60

print(tags.loc[tags["equipment"] == "1번 펌프"])

# ====================
def first_over(col):
  """정상 구간 최댓값을 처음 넘어선 index를 반환합니다."""
  limit = normal[col].max() # 20일 구간(normal)에서 최댓값을 정상 범위로 설정
  over = df.index[df[col] > limit] # 정상 범위를 넘는 limit를 불러온다.
  # print(over)
  # print(first_over("MTR01_VIB_H"))
  # Index([38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
  #      58, 59],
  #     dtype='int64')
  return int(over[0]) + 1 if len(over) else None # index는 0부터 시작하므로 +1

print("-----------------------")
print("[1번 모터]")
for c in MTR:
  print(c, first_over(c))

print("-----------------------")
print("[1번 펌프]")
for c in PMP:
  print(c, first_over(c))

# -----------------------
# [1번 모터]
# MTR01_VIB_H 39
# MTR01_VIB_V 44
# MTR01_VIB_A None
# MTR01_VIB_ACC 22
# -----------------------
# [1번 펌프]
# PMP01_VIB_H 39
# PMP01_VIB_V 38
# PMP01_VIB_A 35
# PMP01_VIB_ACC None

## 모터의 전류와 온도
MTR_OTHER = ["MTR01_CURRENT", "MTR01_TEMP"]
print("-----------------------")
print("[1번 모터의 전류와 온도]")
for c in MTR_OTHER:
  print(c, first_over(c))

# -----------------------
# [1번 모터의 전류와 온도]
# MTR01_CURRENT 49
# MTR01_TEMP 53

# 전류와 온도가 이상반응에 대해서 늦게 반응한다

### 모터 1번의 회전수
# 모터 1번 회전수의 컬럼 이름 (MTR01_RPM)
# 1780, 1450 종류의 숫자가 각각 몇 번 찍히는지
print(df["MTR01_RPM"].value_counts())
# 1780    56
# 1450     4

print(df.loc[df["MTR01_RPM"] == 1780, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]].head(4))
print(df.loc[df["MTR01_RPM"] == 1450, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]].head(4))
#          date  MTR01_VIB_H  MTR01_VIB_ACC  MTR01_RPM
# 0  2026-01-01          1.8           0.52       1780
# 1  2026-01-02          1.9           0.54       1780
# 2  2026-01-03          1.8           0.53       1780
# 3  2026-01-04          2.0           0.55       1780
#           date  MTR01_VIB_H  MTR01_VIB_ACC  MTR01_RPM
# 29  2026-01-30          1.3           0.61       1450
# 30  2026-01-31          1.3           0.63       1450
# 31  2026-02-01          1.4           0.67       1450
# 32  2026-02-02          1.3           0.68       1450

# 설비의 변화가 아닌 회전수(RPM)의 변화로 진동수가 변경되었다.