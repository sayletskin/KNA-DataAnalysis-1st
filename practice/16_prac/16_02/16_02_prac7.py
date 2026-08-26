# 실습7. duplicated로중복찾기와개수
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

# · duplicated로 중복 행 여부를 참·거짓으로 표시
print(df.duplicated().sum()) # 2
# 원본 제외 중복 개수
print(df[df.duplicated()])
#       샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0

# · sum으로 중복 개수 세고 중복 행 직접 확인
print(df.duplicated(keep=False).sum()) # 4
# 원본 중복 모두 포함

# · keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인
