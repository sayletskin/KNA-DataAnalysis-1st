# [1단계] csv 읽기

import os
import csv

path = os.path.join("data", "09_ict_inspection_dirty.csv")

def read_csv():
  rows = []
  try:
    with open(path, "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      header = next(reader)
      # print(header)

      for row in reader:
        # print(row)
        rows.append(row)
      print(f"데이터 행 수: {len(rows)}")
      return header, rows
  except FileNotFoundError:
    print("FileNotFoundError발생")
    return [], []
  
header, rows = read_csv()
# ======================================
# [2단계] 조건 분류
def group_rows_by_category(rows, category_index=0):
    """
    지정한 인덱스(기본값: 0번째 열, 부품/설비명)를 기준 키(Key)로 삼아
    데이터를 그룹별 딕셔너리로 분류합니다.
    """
    grouped_data = {}
    for row in rows:
        if not row:
            continue
        category = row[category_index].strip()
        if category not in grouped_data:
            grouped_data[category] = []
        grouped_data[category].append(row)
    
    print(f"[STEP 2 성공] 총 {len(grouped_data)}개 카테고리/설비로 분류 완료 ({', '.join(grouped_data.keys())})")
    return grouped_data
  



