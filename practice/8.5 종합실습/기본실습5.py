# 실습5. datatime으로 점검 기록 남기기
# 1) os와 datatime을 import
import os, datetime

# 2) listdir로 폴더 파일 수를 구하기
data_folder_count = len(os.listdir("data"))
print(data_folder_count)

# 3) datetime.now로 현재 시각을 담기
now = datetime.datetime.now()
print(now)

# 4) f-string으로 파일 수와 시각을 한 문장으로 출력
print(f"data폴더 파일 수 : {data_folder_count}개\n"
      f"점검 시각 {now}")