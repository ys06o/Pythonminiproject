import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns

# =========================
# 1. 데이터 불러오기
# =========================
df = pd.read_csv("산불_기상_매핑완료_2020_2024.csv", encoding="utf-8-sig")

# 날짜 변환
df["occu_date"] = pd.to_datetime(df["occu_date"], errors="coerce")

# 필요한 컬럼 숫자형 변환
df["평균기온(°C)"] = pd.to_numeric(df["평균기온(°C)"], errors="coerce")
df["일강수량(mm)"] = pd.to_numeric(df["일강수량(mm)"], errors="coerce")
df["평균 풍속(m/s)"] = pd.to_numeric(df["평균 풍속(m/s)"], errors="coerce")
df["ar"] = pd.to_numeric(df["ar"], errors="coerce")  # 피해면적

# 결측 제거
df = df.dropna(subset=[
    "occu_date",
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)",
    "ar"
])

# 월 컬럼 생성
df["월"] = df["occu_date"].dt.month


# =========================
# 2. 가설 1
# 기온이 높고 일강수량이 낮을수록 산불 발생 건수 증가
# =========================

# 날짜별 산불 발생 건수
daily_fire = df.groupby("occu_date").size().reset_index(name="산불발생건수")

# 날짜별 평균 기상값
daily_weather = df.groupby("occu_date")[[
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].mean().reset_index()

# 분석 데이터 생성
analysis_df = daily_fire.merge(
    daily_weather,
    on="occu_date",
    how="inner"
)

# 상관관계 분석
corr = analysis_df[[
    "산불발생건수",
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].corr()

print("===== 가설 1: 상관관계 =====")
print(corr["산불발생건수"])

# 기온과 산불 발생 건수 산점도
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=analysis_df,
    x="평균기온(°C)",
    y="산불발생건수"
)
plt.title("기온과 산불 발생 건수의 관계")
plt.xlabel("평균기온(°C)")
plt.ylabel("산불 발생 건수")
plt.grid(True)
plt.show()

# 강수량과 산불 발생 건수 산점도
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=analysis_df,
    x="일강수량(mm)",
    y="산불발생건수"
)
plt.title("강수량과 산불 발생 건수의 관계")
plt.xlabel("일강수량(mm)")
plt.ylabel("산불 발생 건수")
plt.grid(True)
plt.show()


# =========================
# 3. 가설 2
# 봄철 2~4월은 다른 계절보다 산불 발생 건수와 피해면적이 크다
# =========================

def season_group(month):
    if month in [2, 3, 4]:
        return "봄철(2~4월)"
    else:
        return "그 외 계절"

df["계절구분"] = df["월"].apply(season_group)

# 계절별 산불 발생 건수
season_count = df.groupby("계절구분").size().reset_index(name="산불발생건수")

print("\n===== 가설 2: 계절별 산불 발생 건수 =====")
print(season_count)

plt.figure(figsize=(7, 5))
sns.barplot(
    data=season_count,
    x="계절구분",
    y="산불발생건수"
)
plt.title("봄철과 그 외 계절의 산불 발생 건수 비교")
plt.xlabel("계절 구분")
plt.ylabel("산불 발생 건수")
plt.grid(axis="y")
plt.show()

# 계절별 피해면적 합계
season_area_sum = df.groupby("계절구분")["ar"].sum().reset_index(name="피해면적합계")

print("\n===== 가설 2: 계절별 피해면적 합계 =====")
print(season_area_sum)

plt.figure(figsize=(7, 5))
sns.barplot(
    data=season_area_sum,
    x="계절구분",
    y="피해면적합계"
)
plt.title("봄철과 그 외 계절의 피해면적 합계 비교")
plt.xlabel("계절 구분")
plt.ylabel("피해면적 합계")
plt.grid(axis="y")
plt.show()


# =========================
# 4. 월별 추가 분석
# =========================

monthly_count = df.groupby("월").size().reset_index(name="산불발생건수")

plt.figure(figsize=(9, 5))
sns.barplot(
    data=monthly_count,
    x="월",
    y="산불발생건수"
)
plt.title("월별 산불 발생 건수")
plt.xlabel("월")
plt.ylabel("산불 발생 건수")
plt.grid(axis="y")
plt.show()

monthly_area = df.groupby("월")["ar"].sum().reset_index(name="피해면적합계")

plt.figure(figsize=(9, 5))
sns.barplot(
    data=monthly_area,
    x="월",
    y="피해면적합계"
)
plt.title("월별 피해면적 합계")
plt.xlabel("월")
plt.ylabel("피해면적 합계")
plt.grid(axis="y")
plt.show()


# =========================
# 5. 결과 저장
# =========================
print("\n분석 완료")

import pandas as pd

# 매핑 완료 데이터 불러오기
merged = pd.read_csv("산불_기상_매핑완료_2020_2024.csv", encoding="utf-8-sig")

# 날짜 변환
merged["occu_date"] = pd.to_datetime(merged["occu_date"], errors="coerce")
merged["일시"] = pd.to_datetime(merged["일시"], errors="coerce")

print("===== 1. 전체 데이터 크기 =====")
print(merged.shape)

print("\n===== 2. 날짜 매핑 확인 =====")
print(merged[["occu_date", "일시"]].head(20))

print("\n날짜가 안 맞는 행 개수")
print((merged["occu_date"] != merged["일시"]).sum())

print("\n===== 3. 기상값 결측치 확인 =====")
print(merged[[
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].isnull().sum())

print("\n===== 4. 가까운 기상관측소 거리 확인 =====")
print(merged["기상지점거리_km"].describe())

print("\n거리 50km 초과 개수")
print((merged["기상지점거리_km"] > 50).sum())

print("\n거리 100km 초과 개수")
print((merged["기상지점거리_km"] > 100).sum())

print("\n===== 5. 거리 먼 데이터 확인 =====")
print(merged.sort_values("기상지점거리_km", ascending=False)[[
    "occu_date",
    "adres",
    "x",
    "y",
    "가까운_기상지점명",
    "기상지점거리_km",
    "평균기온(°C)",
    "일강수량(mm)"
]].head(20))

print("\n===== 6. 정상적으로 붙은 샘플 확인 =====")
print(merged[[
    "occu_date",
    "adres",
    "x",
    "y",
    "가까운_기상지점명",
    "기상지점거리_km",
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].head(20))

print("\n===== 7. 월별 산불 발생 건수 =====")
merged["월"] = merged["occu_date"].dt.month
print(merged.groupby("월").size())

print("\n===== 8. 월별 평균 기상값 =====")
print(merged.groupby("월")[[
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].mean())

print("\n===== 9. 가설 1 상관관계 확인 =====")
analysis_df = merged.dropna(subset=[
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
])

daily_fire = analysis_df.groupby("occu_date").size().reset_index(name="산불발생건수")

daily_weather = analysis_df.groupby("occu_date")[[
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].mean().reset_index()

daily_analysis = daily_fire.merge(daily_weather, on="occu_date", how="inner")

corr = daily_analysis[[
    "산불발생건수",
    "평균기온(°C)",
    "일강수량(mm)",
    "평균 풍속(m/s)"
]].corr()

print(corr["산불발생건수"])