import pandas as pd
data = [
    {"이름": "A", "연봉": 100, "event_datetime": "2022-01-01"},
    {"이름": "A", "연봉": 100, "event_datetime": "2022-01-02"},
    {"이름": "B", "연봉": 200, "event_datetime": "2022-01-03"},
]

df = pd.DataFrame(data)

print(df)

result = df.to_dict(orient="records")
print(result)
