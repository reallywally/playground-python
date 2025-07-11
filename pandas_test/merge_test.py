import pandas as pd

# 원본 학생 데이터 생성
student_df = pd.DataFrame(
    {
        "학번": [1, 2, 3],
        "이름": ["A", "B", "C"],
        "입학년도": [2022, 2023, 2024],
        "전공": ["컴퓨터", "영어", "일본어"],
    }
)

temp_df = pd.DataFrame(
    {
        "사번": [1, 2, 3],
        "ㅇㅇ": ["A", "B", "C"],
        "ㅈㅈ": [2022, 2023, 2024],
        "22": ["컴퓨터", "영어", "일본어"],
    }
)

r_df = pd.merge(
    student_df,
    temp_df,
    on=list(set(student_df) & set(temp_df.columns)),
)


print(r_df)
