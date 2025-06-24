import pandas as pd

# 원본 데이터
data = {
    "이름": ["A", "A", "A"],
    "연봉": [1000, 3000, 5000],
    "직업": ["개발자", "개발자", "개발자"],
    "나이": [30, 33, 33],
    "event_datetime": ["2022-01-01", "2025-01-01", "2028-01-01"],
}
df = pd.DataFrame(data)
df["event_datetime"] = pd.to_datetime(df["event_datetime"])

df = df.sort_values("event_datetime").reset_index(drop=True)

# 3. 전체 날짜 범위 생성 (min ~ max)
full_dates = pd.DataFrame({
    "event_datetime": pd.date_range(start=df["event_datetime"].min(), end=df["event_datetime"].max(), freq="D")
})

# 4. full_dates 와 기존 데이터를 날짜 기준으로 병합
merged = pd.merge(full_dates, df, on="event_datetime", how="left")

# 5. 이전 값으로 채우기 (전체 기준)
merged = merged.ffill()


print(merged)


a = [1,2,3]
print(a.remove(2))