# 앞 6시간 뒤 6시간 비교하기
# 송풍량, 송풍압, 송풍기 진동
# 세 값의 변화 방향을 각각 적으세요 (평균)

import pandas as pd

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv", parse_dates=["timestamp"])

print(df.shape) # (720, 6)
print(df.columns.tolist())
# ['timestamp', 'blast_flow_nm3min', 'blast_pressure_kpa',
# 'top_pressure_kpa', 'hot_blast_temp_c', 'blower_vib_mms']

before = df.iloc[:360]
after = df.iloc[360:]

cols = ['blast_flow_nm3min', 'blast_pressure_kpa', 'blower_vib_mms']

print(before[cols].mean().round(1))
print(after[cols].mean().round(1))
# blast_flow_nm3min     5198.7
# blast_pressure_kpa     379.8
# blower_vib_mms           3.4

# blast_flow_nm3min     4977.8
# blast_pressure_kpa     397.7
# blower_vib_mms           3.4

# 송풍량은 낮아지고 송풍압은 높지고 송풍기 진동은 그대로
# 송풍기 기계적 결함보다 고로 내부 통기성 저하 의심
