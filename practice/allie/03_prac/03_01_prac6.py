import pandas as pd

tags = pd.read_csv('data/03-01_유압·열설비_신호_계통태그목록.csv')
df = pd.read_csv('data/03-01_유압·열설비_신호_유압운전.csv')


# [Step 1] 주요 태그 확인

KOREAN = {
  "tag": "태그명",
  "physical_qty": "물리량",
  "unit": "단위",
  "circuit_position": "회로 위치"
}

case_a= tags[tags["tag"].str.startswith("HYD")]
case_a_kr = case_a.rename(columns=KOREAN)
print(case_a_kr[['태그명', '물리량', '단위', '회로 위치']])
#                    태그명 물리량     단위        회로 위치
# 0      HYD01_PRESS_PUMP  압력    bar       펌프 토출부
# 1   HYD01_PRESS_FILT_IN  압력    bar        필터 전단
# 2  HYD01_PRESS_FILT_OUT  압력    bar        필터 후단
# 3       HYD01_DP_FILTER  차압    bar   필터 전후단 계산값
# 4            HYD01_FLOW  유량  L/min     펌프 토출 배관
# 5         HYD01_OILTEMP  온도   degC        탱크 내부
# 6           HYD01_LEVEL  유면      %       탱크 유면계
# 7    HYD01_PUMP_CURRENT  전류      A       펌프 제어반
# 8       HYD01_VALVE_CMD  개도      %  방향 제어 밸브 지령
# 9        HYD01_VALVE_FB  개도      %  방향 제어 밸브 실제

# 강사님 방법
print("==============================")
print(tags.loc[tags["tag"].str.startswith("HYD"), ["tag", "physical_qty", "unit", "circuit_position"]])
# tag physical_qty   unit circuit_position
# 0      HYD01_PRESS_PUMP           압력    bar           펌프 토출부
# 1   HYD01_PRESS_FILT_IN           압력    bar            필터 전단
# 2  HYD01_PRESS_FILT_OUT           압력    bar            필터 후단
# 3       HYD01_DP_FILTER           차압    bar       필터 전후단 계산값
# 4            HYD01_FLOW           유량  L/min         펌프 토출 배관
# 5         HYD01_OILTEMP           온도   degC            탱크 내부
# 6           HYD01_LEVEL           유면      %           탱크 유면계
# 7    HYD01_PUMP_CURRENT           전류      A           펌프 제어반
# 8       HYD01_VALVE_CMD           개도      %      방향 제어 밸브 지령
# 9        HYD01_VALVE_FB           개도      %      방향 제어 밸브 실제

# [Step 2] 정상 구간과 최근 구간 비교

# - HYD01_PRESS_PUMP
# - HYD01_FLOW
# - HYD01_OILTEMP
# - HYD01_LEVEL
# - HYD01_PUMP_CURRENT
col = ["HYD01_PRESS_PUMP", "HYD01_FLOW", "HYD01_OILTEMP", "HYD01_LEVEL", "HYD01_PUMP_CURRENT"]

# 1. 첫 30일 평균
head30_mean = df[col].head(30).mean()

# 2. 마지막 10일 평균
tail10_mean = df[col].tail(10).mean()

for c in col:
    print(f"{c} : {head30_mean[c]}, {tail10_mean[c]}")
# HYD01_PRESS_PUMP : 152.3, 149.5
# HYD01_FLOW : 117.95, 116.95
# HYD01_OILTEMP : 42.35, 48.35
# HYD01_LEVEL : 88.0, 88.0
# HYD01_PUMP_CURRENT : 31.45, 32.45

# [Step 3] 필터 차압 확인

# HYD01_PRESS_FILT_IN
# HYD01_PRESS_FILT_OUT

df["차압"] = df["HYD01_PRESS_FILT_IN"] - df["HYD01_PRESS_FILT_OUT"]
panel1 = df.iloc[:30]
panel2 = df.iloc[30:60]
panel3 = df.iloc[60:90]
# ===================================
print(f"구간 | 시작 차압 | 종료 차압 | 증가폭")
print(f"1~30일 | {panel1['차압'].iloc[0]} | {panel1['차압'].iloc[-1]} | {panel1['차압'].iloc[-1] - panel1['차압'].iloc[0]}")
print(f"31~60일 | {panel2['차압'].iloc[0]} | {panel2['차압'].iloc[-1]} | {panel2['차압'].iloc[-1] - panel2['차압'].iloc[0]}")
print(f"61~90일 | {panel3['차압'].iloc[0]} | {panel3['차압'].iloc[-1]} | {panel3['차압'].iloc[-1] - panel3['차압'].iloc[0]}")
# 구간 | 시작 차압 | 종료 차압 | 증가폭
# 1~30일 | 2.5 | 5.0 | 2.5
# 31~60일 | 2.5 | 6.0 | 3.5
# 61~90일 | 2.5 | 7.0 | 4.5
# ==================================

print("==================================")
result = pd.DataFrame({
    "구간" : ["1~30일", "31~60일", "61~90일"],
    "시작 차압" : [panel1['차압'].iloc[0], panel2['차압'].iloc[0], panel3['차압'].iloc[0]],
    "종료 차압" : [panel1['차압'].iloc[-1], panel2['차압'].iloc[-1], panel3['차압'].iloc[-1]],
    "증가폭" : [panel1['차압'].iloc[-1] - panel1['차압'].iloc[0], panel2['차압'].iloc[-1] - panel2['차압'].iloc[0], panel3['차압'].iloc[-1] - panel3['차압'].iloc[0]]
})

print(result)
#        구간  시작 차압  종료 차압  증가폭
# 0   1~30일    2.5    5.0  2.5
# 1  31~60일    2.5    6.0  3.5
# 2  61~90일    2.5    7.0  4.5

# 강사님 방법
for lo, hi in [(1,30),(31,60),(61,90)]:
  seg = df.iloc[lo-1:hi]
  print(f"{lo}~{hi}일 | {seg['차압'].iloc[0]} | {seg['차압'].iloc[-1]} | {seg['차압'].iloc[-1] - seg['차압'].iloc[0]}")

# 1~30일 | 2.5 | 5.0 | 2.5
# 31~60일 | 2.5 | 6.0 | 3.5
# 61~90일 | 2.5 | 7.0 | 4.5
