# split으로 한 column의 구분화? 하고 구분화 된걸 변수로 만들기
# 딕셔너리를 이용해 map으로 한글화 하기

import pandas as pd
import os

path = os.path.join("data", "dummy", "01-01_철강_공정_개관_설비태그.csv")
df = pd.read_csv(path)
print(df.shape) # (24, 4)
print(df.columns.tolist()) # ['tag', 'unit', 'sample_value', 'note']
print(df['tag'].head(1)) # 0    PL1-SNT-FAN-01-VIB

# 'tag'의 PL1-SNT-FAN-01-VIB 형식을 '-' 구분자로 구분화 하기
split_tag = df['tag'].str.split('-',expand=True)
df['공장'] = split_tag[0]
df['process'] = split_tag[1]
df['장비'] = split_tag[2]
df['번호'] = split_tag[3]
df['계측'] = split_tag[4]

# df['process']을 한글화 하기
pROCESS_KR = {
  "SNT" : "소결",
  "CKO" : "코크스",
  "BF" : "고로",
  "BOF" : "전로",
  "CCM" : "연주",
  "HSM" : "열간압연",
  "CRM" : "냉간압연",
  "UTL" : "유틸리티",
}
df["process_kr"]=df["process"].map(pROCESS_KR)

print(df.groupby("process_kr").size())

