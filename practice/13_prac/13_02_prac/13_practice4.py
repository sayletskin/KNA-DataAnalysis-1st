# 실습4. 부정·목록·범위조건
# 부정·목록 매칭·범위 조건을 각각 적용
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
# print(df.tail(3))
#      샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 27  28  265.0   595.0   33.8   19.0  355.0   주의
# 28  29  218.0  1055.0   20.7   11.0  255.0   양품
# 29  30  218.0  1054.0   21.4    2.0  253.0   불량
# print(len(df)) # 30

# · 물결 기호로 "품질등급"에 고장(불량)이 아닌   설비만 뒤집어 추출
df_not = df[~( df["품질등급"] == "불량" )]
print(len(df_not)) # 24

# · isin으로 품질등급이 특정 목록에 속하는 행 추출
df_isin = df[ df["품질등급"].isin(["불량"])]
print(len(df_isin)) # 6

# · between으로 실린더압력이 지정 범위에 든 행 추출
df_between = df[ df["실린더압력"].between(210, 220) ]
print(len(df_between)) # 24
