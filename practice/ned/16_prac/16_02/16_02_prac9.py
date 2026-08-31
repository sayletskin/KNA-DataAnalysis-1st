import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
# 실습9. reset_index로인덱스정리

# · drop_duplicates로 중복을 제거
df_clean = df.drop_duplicates()


# · reset_index로 인덱스를 0부터 다시 매기기
df_clean_idxreset = df_clean.reset_index(drop=True)


# · 인덱스 최솟값·최댓값으로 연속성 확인
print(df_clean_idxreset.index.min(), df_clean_idxreset.index.max())
print(len(df_clean_idxreset))
# 인덱스 0(min) ~ 199(max)
# 총 200개