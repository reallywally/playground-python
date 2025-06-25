import pandas as pd

# pandas 출력 설정 - 전체 데이터 표시
pd.set_option('display.max_rows', None)  # 모든 행 표시
pd.set_option('display.max_columns', None)  # 모든 열 표시
pd.set_option('display.width', None)  # 출력 너비 제한 해제
pd.set_option('display.max_colwidth', None)  # 열 너비 제한 해제

entities = ["이름"]
start_date = pd.to_datetime("2022-02-10")
end_date = pd.to_datetime("2022-03-30")


# 예제 데이터
data = {
    "이름": ["A", "A", "A", "B", "B"],
    "연봉": [1000, 3000, 5000, 1500, 3500],
    "직업": ["개발자", "기획자", "개발자", "디자이너", "디자이너"],
    "나이": [30, 30, 33, 28, 30],
    "event_datetime": [
        "2022-02-10",
        "2022-03-15",
        "2025-06-20",
        "2022-02-05",
        "2024-04-22",
    ],
}
df = pd.DataFrame(data)

df["event_datetime"] = pd.to_datetime(df["event_datetime"])

# 전체 날짜 생성
full_dates = pd.date_range(start=start_date, end=end_date, freq="D")

# entity 단위 추가
entity_columns = df[entities].drop_duplicates().values.flatten()
key_columns = entities + ["event_datetime"]
full_index = pd.MultiIndex.from_product([entity_columns, full_dates], names=key_columns)
full_df = pd.DataFrame(index=full_index).reset_index()


# 병합 후 ffill
merged = pd.merge(full_df, df, on=key_columns, how="left")
merged = merged.sort_values(key_columns)
merged = merged.ffill()

# 결과 출력
print(merged)
