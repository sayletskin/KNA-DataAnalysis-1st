import pandas as pd

# CSV 불러오기
df = pd.read_csv("data/03-01_유압·열설비_신호_가열로온도.csv")


# =========================
# Step 2
# 앞 20일 평균 편차
# =========================

df["Z1_편차"] = df["FUR01_Z1_TEMP_R"] - df["FUR01_Z1_TEMP_L"]
df["Z2_편차"] = df["FUR01_Z2_TEMP_R"] - df["FUR01_Z2_TEMP_L"]
df["Z3_편차"] = df["FUR01_Z3_TEMP_R"] - df["FUR01_Z3_TEMP_L"]

normal = df.iloc[:20]

print("=== Step 2 ===")
print("Z1 평균 편차:", normal["Z1_편차"].mean())
print("Z2 평균 편차:", normal["Z2_편차"].mean())
print("Z3 평균 편차:", normal["Z3_편차"].mean())


# =========================
# Step 3
# 1/20/40/60일차 편차
# =========================

days = [1, 20, 40, 60]

result = df.iloc[[day - 1 for day in days]][
    ["Z1_편차", "Z2_편차", "Z3_편차"]
]

result.index = [f"{day}일차" for day in days]

print("\n=== Step 3 ===")
print(result)

increase = result.loc["60일차"] - result.loc["1일차"]

print("\n1일차 → 60일차 증가량")
print(increase)

print("\n가장 크게 증가한 존:", increase.idxmax())


# =========================
# Step 4
# Z2 좌우 온도
# =========================

result_z2 = df.iloc[[day - 1 for day in days]][
    ["FUR01_Z2_TEMP_L", "FUR01_Z2_TEMP_R"]
]

result_z2.index = [f"{day}일차" for day in days]

print("\n=== Step 4 ===")
print(result_z2)

print("\n좌측 변화:",
      result_z2["FUR01_Z2_TEMP_L"].iloc[-1]
      - result_z2["FUR01_Z2_TEMP_L"].iloc[0])

print("우측 변화:",
      result_z2["FUR01_Z2_TEMP_R"].iloc[-1]
      - result_z2["FUR01_Z2_TEMP_R"].iloc[0])


# =========================
# Step 5
# 소재 온도 + 라인 속도
# =========================

days = [1, 20, 44, 45, 60]

result = df.iloc[[day - 1 for day in days]][
    ["FUR01_MAT_TEMP", "FUR01_LINE_SPEED"]
]

result.index = [f"{day}일차" for day in days]

print("\n=== Step 5 ===")
print(result)