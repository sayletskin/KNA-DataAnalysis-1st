import pandas as pd

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv")
# print(df.shape) # (720, 6)
# df.info()

# print(df.columns.tolist())
# ['timestamp', 'blast_flow_nm3min', 'blast_pressure_kpa',
#  'top_pressure_kpa', 'hot_blast_temp_c', 'blower_vib_mms']


### 1. csv에서 datetime 데이터 불러오기(메서드 이용)
print(df["timestamp"].dtype) # str
df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df["timestamp"].dtype) # datetime64[us]

### 2. read_csv() 의 옵션값 이용
df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv", parse_dates=["timestamp"])
print(df["timestamp"].dtype) # datetime64[us]

# timestamp의 시간 간격
gaps = df["timestamp"].diff().value_counts()
print(gaps)
# timestamp
# 0 days 00:01:00    719
# 720행의 데이터 중 719개의 타임 간격이 1분 차이로 동일

# 송풍량, 소풍압, 송풍기 진동
print(df[["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]].describe().round(1))
#        blast_flow_nm3min  blast_pressure_kpa  blower_vib_mms
# count              720.0               720.0           720.0
# mean              5088.2               388.8             3.4
# std                159.6                13.0             0.1
# min               4681.8               372.8             3.2
# 25%               4977.5               379.4             3.3
# 50%               5180.8               381.7             3.4
# 75%               5202.5               398.3             3.4
# max               5258.2               421.4             3.6

### 이동 평균: N분간의 흔들림을 확인해서 송풍량의 장기적인 방향을 보는 지표
# 통기성이 나빠지면 공기가 원료층을 통과하기 어려워져서 실제 들어가는 풍량이 감소할 수 있음

# 15분 간격 이동 평균 구하기
df["flow_na"] = df["blast_flow_nm3min"].rolling(window=15).mean()
print(df["flow_na"].head(3).tolist()) # [nan, nan, nan]

print(round(df["flow_na"].iloc[14], 1), round(df["flow_na"].iloc[400], 1))
# 5201.5, 5200.8 << 차이가 크지 않음, 이 값으로 통기성 악화가 보이지 않음
# 현재 csv에서는 송풍량으로 통기성 악화를 확인불가

### 이동 표준편차
df["top_sd"] = df["top_pressure_kpa"].rolling(window=30).std()

print(round(df["top_sd"].iloc[200], 1), round(df["top_sd"].iloc[560], 1))
# 2.6 4.3
# 같은 노정압 계측, 뒤쪽 구간에서 흔들림이 크게 늘어난 것을 이동 표준편차로 확인할 수 있음
