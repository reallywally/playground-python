import pandas as pd
from functools import reduce
import operator

df = pd.DataFrame(
    {
        "inon_no": ["0009428122", "0002351516", "2222222"],
        "test_column": ["11111111", "2222222222", "2222222"],
        "학번": [1, 2, 3],
        "이름": ["A", "B", "C"],
        "입학년도": [2022, 2023, 2024],
        "전공": ["컴퓨터", "영어", "일본어"],
    }
)
print(df)
condition_list = [
    {"inon_no": "0009428122", "test_column": "11111111"},
    {"inon_no": "0002351516", "test_column": "2222222222"},
]

# 조건 생성
conditions = []
for cond in condition_list:
    sub_cond = reduce(operator.and_, [(df[k] == v) for k, v in cond.items()])
    conditions.append(sub_cond)

# 최종 조건 (OR로 결합)
if conditions:
    condition_result = reduce(operator.or_, conditions)
else:
    condition_result = pd.Series([False] * len(df))  # 빈 조건인 경우 전체 False

# 필터링 결과
filtered_df = df[condition_result]
print(filtered_df)
