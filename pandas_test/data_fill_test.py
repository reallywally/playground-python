import pandas as pd

# pandas 출력 설정 - 전체 데이터 표시
pd.set_option("display.max_rows", None)  # 모든 행 표시
pd.set_option("display.max_columns", None)  # 모든 열 표시
pd.set_option("display.width", None)  # 출력 너비 제한 해제
pd.set_option("display.max_colwidth", None)  # 열 너비 제한 해제

EVENT_TIMESTAMP = "event_timestamp"


def fill_by_day(df, entities, start, end):
    df[EVENT_TIMESTAMP] = pd.to_datetime(df[EVENT_TIMESTAMP])

    # 전체 날짜 생성
    full_date_df = pd.date_range(start=start, end=end, freq="D")

    # 필요한 컬럼 정리
    entity_columns = df[entities].drop_duplicates().values.flatten()
    merge_columns = entities + [EVENT_TIMESTAMP]
    value_columns = [column for column in df.columns if column not in entities]

    # merge할 df 생성
    full_index = pd.MultiIndex.from_product(
        [entity_columns, full_date_df], names=merge_columns
    )
    full_df = pd.DataFrame(index=full_index).reset_index()

    # 병합 후 ffill
    merged = pd.merge(full_df, df, on=merge_columns, how="left")
    merged = merged.sort_values(merge_columns)
    merged[value_columns] = merged.groupby(entities)[value_columns].ffill()

    return merged


def fill_by_month(df, entities, start, end):
    df[EVENT_TIMESTAMP] = pd.to_datetime(df[EVENT_TIMESTAMP])
    df["year_month"] = df[EVENT_TIMESTAMP].dt.to_period("M").dt.to_timestamp()

    # 월 범위 생성
    month_df = pd.date_range(start=start - pd.DateOffset(months=1), end=end, freq="MS")

    # 필요한 컬럼 정리
    entity_values = df[entities].drop_duplicates().values.flatten()
    merge_columns = entities + ["year_month"]
    value_columns = [column for column in df.columns if column not in entities]

    full_index = pd.MultiIndex.from_product(
        [entity_values, month_df], names=merge_columns
    )
    full_df = pd.DataFrame(index=full_index).reset_index()

    # 병합 후 ffill
    merged = pd.merge(full_df, df, on=merge_columns, how="left")
    merged = merged.sort_values(merge_columns)
    merged[value_columns] = merged.groupby(entities)[value_columns].ffill()
    # merged = merged.ffill()

    return merged


def fill_by_year(df, entities, start, end):
    df[EVENT_TIMESTAMP] = pd.to_datetime(df[EVENT_TIMESTAMP])
    df["year"] = pd.to_datetime(df[EVENT_TIMESTAMP].dt.year.astype(str) + "-01-01")

    years_df = pd.date_range(start=f"{start}-01-01", end=f"{end}-01-01", freq="YS")

    df_temp = df[entities].copy()
    df_temp["key"] = 1
    years_df["key"] = 1

    # 필요한 컬럼 정리
    entity_values = df[entities].drop_duplicates().values.flatten()
    merge_columns = entities + ["year"]
    value_columns = [column for column in df.columns if column not in entities]

    full_index = pd.MultiIndex.from_product(
        [entity_values, years_df], names=merge_columns
    )
    full_df = pd.DataFrame(index=full_index).reset_index()

    # 병합 후 ffill
    merged_df = pd.merge(full_df, df, on=merge_columns, how="left")
    merged_df = merged_df.sort_values(merge_columns)
    merged_df[value_columns] = merged_df.groupby(entities)[value_columns].ffill()

    # event_timestamp 값이 NaT인 행 제외
    merged_df = merged_df[merged_df[EVENT_TIMESTAMP].notna()]

    return merged_df


    print(c)


if __name__ == "__main__":
    entities = ["이름"]
    # start = pd.to_datetime("2022-02-10")
    # end = pd.to_datetime("2022-03-30")

    start = 2020
    end = 2025

    # 예제 데이터
    data = {
        "이름": ["A", "A", "A", "B", "B"],
        "연봉": [1000, 3000, 5000, 1500, 3500],
        "직업": ["개발자", "기획자", "개발자", "디자이너", "디자이너"],
        "나이": [30, 30, 33, 28, 30],
        "event_timestamp": [
            "2022-02-10",
            "2022-03-15",
            "2025-06-20",
            "2022-02-05",
            "2024-04-22",
        ],
    }
    df = pd.DataFrame(data)
    print(fill_by_month(df, entities, start, end))
