import pandas as pd
import polars as pl # pip install polars
import duckdb # pip install duckdb

# ==============================================================================
# [1] Pandas (판다스)
# - 특징: 파이썬 데이터 분석의 표준 라이브러리. 행/열 인덱스 기반의 직관적인 조작 지원.
# - 장점: 가장 넓은 생태계, 방대한 레퍼런스, 다양한 서드파티 라이브러리(scikit-learn 등)와의 호환성.
# - 단점: 기본적으로 싱글 코어 연산 위주라 대용량 데이터에서 속도가 느리고, 메모리 복사 비용이 큼.
# ==============================================================================


# 1.1 CSV 파일 전체를 메모리로 읽어 들임
df_pd = pd.read_csv("sales_data.csv")

# 1.2 조건 필터링
# Pandas에서는 슬라이싱 시 뷰(View)와 복사본(Copy) 구분을 명확히 하기 위해 .copy()를 명시하는 편이 안전함
df_pd_filtered = df_pd[df_pd["category"] == "Electronics"].copy()

# 1.3 파생 컬럼 생성 (단가 * 수량)
df_pd_filtered["total_sales"] = (
    df_pd_filtered["quantity"] * df_pd_filtered["unit_price"]
)

# 1.4 그룹화 및 집계 연산
# groupby 후 집계 시 인덱스로 변환된 'category'를 다시 일반 컬럼으로 꺼내기 위해 .reset_index() 필요
res_pd = (
    df_pd_filtered.groupby("category")
    .agg(total_sales=("total_sales", "sum"), total_qty=("quantity", "sum"))
    .reset_index()
)

print("--- [Pandas 결과] --- \n", res_pd)


# ==============================================================================
# [2] Polars (폴라즈)
# - 특징: Rust 기반으로 작성된 초고속 데이터프레임 라이브러리. Apache Arrow 메모리 포맷 사용.
# - 장점: 멀티스레딩 병렬 처리 지원, 메모리 효율 우수, 표현식(Expression) 기반의 파이프라인 구성.
# - 단점: Pandas와 문법 차이가 존재하여 러닝 커브가 있고, 일부 레거시 라이브러리와 직접 호환되지 않음.
# ==============================================================================

res_pl = (
    pl.read_csv("sales_data.csv")
    # 2.1 pl.col() 표현식을 활용한 고속 벡터화 필터링
    .filter(pl.col("category") == "Electronics")
    # 2.2 with_columns(): 원본 불변성을 유지하며 새 컬럼 추가
    .with_columns(
        (pl.col("quantity") * pl.col("unit_price")).alias("total_sales")
    )
    # 2.3 group_by() & agg(): 병렬 그룹 집계 연산 수행 (별도의 인덱스 리셋 불필요)
    .group_by("category").agg(
        pl.col("total_sales").sum().alias("total_sales"),
        pl.col("quantity").sum().alias("total_qty"),
    )
)

print("\n--- [Polars 결과] --- \n", res_pl)


# ==============================================================================
# [3] DuckDB (덕디비)
# - 특징: 분석용(OLAP) 임베디드 SQL 데이터베이스 엔진.
# - 장점: 별도 서버 설치 없이 파일/메모리에서 바로 실행 가능, 표준 SQL 지원,
#         CSV/Parquet 파일을 메모리에 전부 올리지 않고도 스트리밍 쿼리 가능.
# - 단점: 파이썬 객체 지향 메서드 체이닝보다는 SQL 쿼리 문자열 중심이므로 코드 스타일이 달라짐.
# ==============================================================================

# 3.1 파일 경로를 테이블처럼 직접 쿼리하여 메모리 로딩과 필터/집계를 한 번에 최적화 수행
res_duckdb = duckdb.sql("""
    SELECT 
        category,
        SUM(quantity * unit_price) AS total_sales,
        SUM(quantity) AS total_qty
    FROM 'sales_data.csv'
    WHERE category = 'Electronics'
    GROUP BY category
""").df()  # 3.2 결과를 Pandas DataFrame 형태로 바로 변환하여 수신

print("\n--- [DuckDB 결과] --- \n", res_duckdb)