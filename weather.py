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

# 기상 데이터 없는 날 제거
df = df.dropna(subset=["평균기온(°C)", "일강수량(mm)"])
df["월"] = df["occu_date"].dt.month

# =========================================================
# 가설 1: 기온이 높고 강수량이 낮을수록 건수가 증가한다
# =========================================================

temp_bins = range(-10, 45, 5)
df["기온구간"] = pd.cut(df["평균기온(°C)"], bins=temp_bins)
temp_summary = df.groupby("기온구간", observed=False).size().reset_index(name="발생건수")

plt.figure(figsize=(10, 5))
sns.barplot(data=temp_summary, x="기온구간", y="발생건수", color="salmon")
plt.title("1. 기온이 높을 때 산불이 많이 날까?", fontsize=14, fontweight='bold')
plt.xlabel("기온 구간 (°C)")
plt.ylabel("산불 발생 건수")
plt.show()

rain_bins = [-1, 0, 1, 5, 10, 500]
rain_labels = ["0 (비안옴)", "1미만", "1~5", "5~10", "10이상"]
df["강수구간"] = pd.cut(df["일강수량(mm)"], bins=rain_bins, labels=rain_labels)
rain_summary = df.groupby("강수구간", observed=False).size().reset_index(name="발생건수")

plt.figure(figsize=(10, 5))
sns.barplot(data=rain_summary, x="강수구간", y="발생건수", color="skyblue")
plt.title("2. 강수량이 낮을 때 산불이 많이 날까?", fontsize=14, fontweight='bold')
plt.xlabel("일강수량 구간 (mm)")
plt.ylabel("산불 발생 건수")
plt.show()

heatmap_data = df.groupby(["기온구간", "강수구간"], observed=False).size().unstack(fill_value=0)

plt.figure(figsize=(12, 7))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlOrRd")
plt.title("3. 결론: 어떤 기상 조건(기온+강수)에서 산불이 가장 많이 났나?", fontsize=14, fontweight='bold')
plt.xlabel("일강수량 구간 (mm)")
plt.ylabel("평균 기온 구간 (°C)")
plt.show()


# =========================================================
# 가설 2: 봄철(3~5월)이 더 위중하다
# =========================================================

df["계절구분"] = df["월"].apply(lambda x: "봄철(3~5월)" if x in [3, 4, 5] else "그 외 계절")
season_stats = df.groupby("계절구분").agg(
    발생건수=("occu_date", "count"),
    피해면적합계=("ar", "sum")
).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=season_stats, x="계절구분", y="발생건수", hue="계절구분", palette=["red", "gray"], legend=False)
plt.title("4. 봄철 vs 다른 계절 발생 건수 비교", fontsize=14, fontweight='bold')
plt.xlabel("계절구분")
plt.ylabel("발생건수")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=season_stats, x="계절구분", y="피해면적합계", hue="계절구분", palette=["red", "gray"], legend=False)
plt.title("5. 봄철 vs 다른 계절 피해면적 비교", fontsize=14, fontweight='bold')
plt.xlabel("계절구분")
plt.ylabel("피해면적합계")
plt.show()