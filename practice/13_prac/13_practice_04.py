# 실습4. loc와 iloc로 행 선택하기
# 라벨 기준 loc와 번호 기준 iloc로 행 선택, 범위 차이 확인
import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')

# loc로 라벨 기준 단일 행 선택
print(df.loc[0, '품질등급'])

# iloc로 번호 기준 단일 행 선택
# df.iloc[0] -> 특정 row number인 row의 Serise 추출
# .. ['품질등급'] -> 해당 serise에서 '품질등급' 컬럼의 내용만 추출
print(df.iloc[0]['품질등급'])

# 범위 선택으로 loc 끝 포함·iloc 끝 제외 차이 확인
# 두 결과 동일한지 다른지 주석
print(len(df.loc[0:2])) # 3, 0~2
print(len(df.iloc[0:2])) # 2, 0~1