import numpy as np
import pandas as pd

# 원본 학생 데이터 생성
student_df = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "이름": ["A", "A", "A"],
        "입학년도": [2022, 2023, 2024],
        "전공": [np.nan, np.nan, "일본어"],
        "학년": [np.nan, np.nan, 3],
    }
)
print("원본 데이터:")
print(student_df)

# 전공 컬럼의 빈 값을 뒤에서부터 채우기
student_df[["전공", "학년"]] = student_df.groupby(["id", "이름"])[["전공", "학년"]].bfill()

print("\n결과:")
print(student_df)