import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")

PROCESS_KR = {
  "SNT" : "소결",
  "CKO" : "코크스",
  "BF" : "고로",
  "BOF" : "전로",
  "CCM" : "연주",
  "HSM" : "열간압연",
  "CRM" : "냉간압연",
  "UTL" : "유틸리티",
}

STAGE_KR = {
  "SNT" : "상공정",
  "CKO" : "상공정",
  "BF" : "상공정",
  "BOF" : "상공정",
  "CCM" : "상공정",
  "HSM" : "하공정",
  "CRM" : "하공정",
  "UTL" : "유틸리티",
}

MEASURE_KR = {
  "VIB" : "진동",
  "CUR" : "전류",
  "TMP" : "온도",
  "PRS" : "압력",
  "FLW" : "유량",
  "SPD" : "속도",
  "LVL" : "레벨",
}

split_cols = df["tag"].str.split("-", expand=True)
df["plant"]=split_cols[0]
df["process"]=split_cols[1]
df["equip"]=split_cols[2]
df["unit_no"]=split_cols[3]
df["measure"]=split_cols[4]

df["process_kr"]=df["process"].map(PROCESS_KR)

print(df.groupby("process_kr").size())
# 고로      4
# 냉간압연    3
# 소결      3
# 연주      3
# 열간압연    4
# 유틸리티    3
# 전로      2
# 코크스     2
# 가장 많은 공정 : 고로, 열간압연

# 상공정 하공정과 관련된 stage 컬럼 추가
df["stage"] = df["process"].map(STAGE_KR).fillna("미등록")
# print(df.head())
print(df.groupby("stage").size())
# 상공정     14
# 유틸리티     3
# 하공정      7
# print(df["stage"].value_counts())
# 가장 많은 공정 : 상공정

df["measure_kr"] = df["measure"].map(MEASURE_KR)

print(df.groupby("measure_kr").size().sort_values(ascending=False, kind="stable"))
# 온도    6
# 압력    5
# 전류    5
# 진동    4
# 유량    3
# 속도    1
# 가장 많은 물리량 : 온도