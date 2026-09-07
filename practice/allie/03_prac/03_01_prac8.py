import pandas as pd

df = pd.read_csv('data/03-02_센서_고장_판별_이상구간샘플_127_260902_Question_2.csv')

# case  B : 유압,가열로 계통
# -> HYD, FUR 컬럼

# 시간 컬럼을 날짜/시간 형식으로 변환
df["timestamp"] = pd.to_datetime(df["timestamp"])

# ① HYD02_PRESS
# 같은 값이 연속해서 몇 번 나타나는지 확인
press_same = df["HYD02_PRESS"].eq(
    df["HYD02_PRESS"].shift()
)

print("HYD02_PRESS 연속 동일값:")
print(press_same.groupby((~press_same).cumsum()).sum().max())


# ② HYD02_PRESS_ACC
# 최대값 확인
max_press_acc = df["HYD02_PRESS_ACC"].max()

print("HYD02_PRESS_ACC 최대값:", max_press_acc)

# 최대값과 같은 데이터가 몇 개 있는지 확인
print("최대값 개수:",
      (df["HYD02_PRESS_ACC"] == max_press_acc).sum())


# ③ HYD02_FLOW
# 이동표준편차로 흔들림 폭 확인
df["FLOW_STD"] = df["HYD02_FLOW"].rolling(window=10).std()

print("\nHYD02_FLOW 이동표준편차:")
print(df[["timestamp", "HYD02_FLOW", "FLOW_STD"]].tail(20))


# ④ FUR02_TEMP_Z1
# 평균과 최대값 확인
print("\nFUR02_TEMP_Z1 통계:")
print(df["FUR02_TEMP_Z1"].describe())

# 1400 이상인 값 확인
spike = df[df["FUR02_TEMP_Z1"] >= 1400]

print("\nFUR02_TEMP_Z1 스파이크 후보:")
print(spike[["timestamp", "FUR02_TEMP_Z1"]])