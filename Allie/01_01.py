tag = "PL1-SNT-FAN-01-VIB"
# 공장-공정-설비-일련번호-계측항목

parts = tag.split("-")
print(parts) # ['PL1', 'SNT', 'FAN', '01', 'VIB']

# - 기준으로 나눈 결과 문자열을 변수에 다로 저장
plant = parts[0] # 공장
process = parts[1] # 공정
equip = parts[2] # 설비
unit_no = parts[3] # 일련번호
measure = parts[4] # 측정항목

print(plant, process, equip, unit_no, measure)
# PL1 SNT FAN 01 VIB

# 공정 데이터 규칙
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

# 전로 출력하기
print(PROCESS_KR["BOF"])
print(PROCESS_KR.get("BOF", "미등록"))
print(PROCESS_KR.get("BOF1", "미등록")) # .get 방법을 권장

# 계측항목 규칙표
MEASURE_KR = {
  "VIB" : "진동",
  "CUR" : "전류",
  "TMP" : "온도",
  "PRS" : "압력",
  "FLW" : "유량",
  "SPD" : "속도",
  "LVL" : "레벨",
}

# 압력 출력하기
print(MEASURE_KR.get("PRS", "미등록"))

import pandas as pd

df = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv")
print(df.shape) # (24, 4)
print(df.columns.tolist())
# ['tag', 'unit', 'sample_value', 'note']


# "공정별로 몇 개의 태그가 있는지 세어보기"
split_cols = df["tag"].str.split("-", expand=True)
df["plant"]=split_cols[0]
df["process"]=split_cols[1]
df["equip"]=split_cols[2]
df["unit_no"]=split_cols[3]
df["measure"]=split_cols[4]

print(df.loc[0,"process"], df.loc[0,"measure"])

df["process_kr"]=df["process"].map(PROCESS_KR)
print(df[["tag","process_kr"]].head(3))

print(df.groupby("process_kr").size())
# '''
# process_kr
# 고로      4
# 냉간압연    3
# 소결      3
# 연주      3
# 열간압연    4
# 유틸리티    3
# 전로      2
# 코크스     2
# '''

