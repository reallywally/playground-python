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

# df = df.groupby(["이름"], group_keys=False).ffill()
# df = df.groupby(["이름"]).apply(lambda x: x.ffill()).reset_index(drop=True)
df[["연봉", "직업", "나이"]] = df.groupby("이름")[["연봉", "직업", "나이"]].ffill()

print(df)
