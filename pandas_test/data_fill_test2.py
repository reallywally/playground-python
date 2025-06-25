import pandas as pd

# 1. 예제 데이터
data = {
    "이름": ["A", "A", "A", "B", "B"],
    "연봉": [1000, 3000, 5000, 1500, 3500],
    "직업": ["개발자"] * 5,
    "나이": [30, 33, 33, 28, 31],
    "event_datetime": [
        "2022-01-01",
        "2022-01-03",
        "2022-01-06",
        "2022-01-02",
        "2022-01-04",
    ],
}

df = pd.DataFrame(data)
df["event_datetime"] = pd.to_datetime(df["event_datetime"])

# 2. 날짜 범위 지정
start_date = pd.to_datetime("2022-01-01")
end_date = pd.to_datetime("2022-01-07")

# 3. 사람 × 날짜 조합 생성
people = df["이름"].unique()
print(people)
full_dates = pd.date_range(start=start_date, end=end_date, freq="D")
full_index = pd.MultiIndex.from_product(
    [people, full_dates], names=["이름", "event_datetime"]
)
full_df = pd.DataFrame(index=full_index).reset_index()

# 4. 원본 데이터 준비
df_small = df[["이름", "event_datetime", "연봉", "직업", "나이"]].sort_values(
    ["이름", "event_datetime"]
)

# 5. 병합 및 ffill
merged = pd.merge(full_df, df_small, on=["이름", "event_datetime"], how="left")
merged = merged.sort_values(["이름", "event_datetime"])
merged = merged.groupby("이름").ffill()

# 6. 결과 확인
print(merged)
