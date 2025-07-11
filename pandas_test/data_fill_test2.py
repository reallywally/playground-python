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


# 1. 모든 입학년도와 학생의 조합 생성
years = [2021, 2022, 2023, 2024]
students = student_df[["학번", "이름"]].drop_duplicates()

# Cross join을 위한 더미 키 생성
students["key"] = 1
years_df = pd.DataFrame({"입학년도": years, "key": 1})

# Cross join 수행
result = pd.merge(years_df, students, on="key").drop("key", axis=1)

print("모든 조합 생성 결과:")
print(result)
print("\n" + "=" * 50 + "\n")

# 2. 원본 데이터와 merge하여 전공 정보 추가
# 학번, 이름, 입학년도가 모두 일치하는 경우에만 전공 정보를 가져옴
final_result = pd.merge(
    result,
    student_df[["학번", "이름", "입학년도", "전공"]],
    on=["학번", "이름", "입학년도"],
    how="left",
)

# 전공 컬럼의 NaN을 빈 문자열로 변경
final_result["전공"] = final_result["전공"].fillna("")

# 컬럼 순서 정렬
final_result = final_result[["입학년도", "학번", "이름", "전공"]]

# 입학년도, 학번 순으로 정렬
final_result = final_result.sort_values(["입학년도", "학번"]).reset_index(drop=True)

print("최종 결과:")
print(final_result)
