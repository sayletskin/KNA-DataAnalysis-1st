import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')

# 실습 4. 삭제 손실 비교
# 삭제 방식별 남는 행 수와 손실률을 표로 비교

# 단계
# · 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# · 방식과 행 수를 하나의 표로 모으기

# 비교 = pd.DataFrame({
#     '방식': ['원본', '행삭제', 'thresh20'],
#     '행': [len(df), len(df.dropna()), len(df.dropna(thresh = 20))]
# })

# 비교['손실률'] = ((1 - 비교['행'] / len(df)) * 100) .round(2)

# print(비교)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# 위 코드는 너무 고급기술 - DF의 더 깊은 이해 경험 필요
# 여러분은 그냥 개별 3가지 항목들을 따로따로 계산시켜 출력해도 괜찮아요
비교 = pd.DataFrame({
    '방식' : ['원본', '행삭제', 'thresh20'],
    '행' : [len(df), len(df.dropna()), len(df.dropna(thresh=20))],
    '손실률' : [
        round((1-len(df)/len(df))*100, 2), 
        round((1-len(df.dropna())/len(df))*100, 2), 
        round((1-len(df.dropna(thresh=20))/len(df))*100, 2)
        ]
})

print(비교)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# · 원본 대비 손실률을 백분율로 계산해 나란히 보기

# 예상 결과
# 행삭제 손실 약 70%, thresh 손실 약 35%