import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanfont

# 1. 데이터 로드 및 전처리
df = pd.read_csv("산불_기상_매핑완료_2020_2024.csv", encoding="utf-8-sig")

df["occu_date"] = pd.to_datetime(df["occu_date"], errors="coerce")
df["평균기온(°C)"] = pd.to_numeric(df["평균기온(°C)"], errors="coerce")
df["일강수량(mm)"] = pd.to_numeric(df["일강수량(mm)"], errors="coerce")
df["ar"] = pd.to_numeric(df["ar"], errors="coerce")

df = df.dropna(subset=["평균기온(°C)", "일강수량(mm)"])

# =========================================================
# 가설 1 시각화 (개별 막대 그래프는 기존과 동일)
# =========================================================

# [그래프 1-1] 기온 구간별 발생 건수
temp_bins = range(-10, 45, 5)
df["기온구간"] = pd.cut(df["평균기온(°C)"], bins=temp_bins)
temp_summary = df.groupby("기온구간", observed=False).size().reset_index(name="발생건수")

plt.figure(figsize=(10, 6))
sns.barplot(data=temp_summary, x="기온구간", y="발생건수", color="#E74C3C")
plt.title("가설 1-1: 기온 구간별 산불 발생 건수", fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# [그래프 1-2] 일강수량 구간별 발생 건수
rain_bins = [-1, 0, 1, 5, 10, 500]
rain_labels = ["0", "1미만", "1~5", "5~10", "10이상"]
df["강수구간"] = pd.cut(df["일강수량(mm)"], bins=rain_bins, labels=rain_labels)
rain_summary = df.groupby("강수구간", observed=False).size().reset_index(name="발생건수")

plt.figure(figsize=(10, 6))
sns.barplot(data=rain_summary, x="강수구간", y="발생건수", color="#3498DB")
plt.title("가설 1-2: 일강수량 구간별 산불 발생 건수", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# [그래프 1-3] 수정된 히트맵: 기온과 강수량에 따른 발생 건수 분포
# 기온(행)과 강수량(열)을 교차하여 발생 건수를 집계한 피벗 테이블 생성
heatmap_data = df.groupby(["기온구간", "강수구간"], observed=False).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlOrRd", cbar_kws={'label': '산불 발생 건수'})
plt.title("가설 1-3: 기온 및 강수량별 산불 발생 빈도 (히트맵)", fontsize=14, fontweight='bold')
plt.xlabel("일강수량 구간 (mm)")
plt.ylabel("평균 기온 구간 (°C)")
plt.tight_layout()
plt.show()

# =========================================================
# 가설 2: 봄철(2~4월) 비교 (기존 유지)
# =========================================================
df["월"] = df["occu_date"].dt.month
df["계절구분"] = df["월"].apply(lambda x: "봄철(2~4월)" if x in [2, 3, 4] else "그 외 계절")
season_stats = df.groupby("계절구분").agg(발생건수=("occu_date", "count"), 피해면적합계=("ar", "sum")).reset_index()

# 발생 건수 비교
plt.figure(figsize=(8, 6))
sns.barplot(data=season_stats, x="계절구분", y="발생건수", hue="계절구분", palette=["#E74C3C", "#95A5A6"], legend=False)
plt.title("가설 2-1: 계절별 산불 발생 건수 비교", fontsize=14, fontweight='bold')
plt.show()

# 피해면적 비교
plt.figure(figsize=(8, 6))
sns.barplot(data=season_stats, x="계절구분", y="피해면적합계", hue="계절구분", palette=["#E74C3C", "#95A5A6"], legend=False)
plt.title("가설 2-2: 계절별 산불 피해면적 합계 비교", fontsize=14, fontweight='bold')
plt.show()