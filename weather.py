import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import koreanfont

# =========================
# 1. 데이터 불러오기
# =========================
df = pd.read_csv("산불_기상_매핑완료_2020_2024.csv", encoding="utf-8-sig")

df["occu_date"] = pd.to_datetime(df["occu_date"], errors="coerce")
df["평균기온(°C)"]   = pd.to_numeric(df["평균기온(°C)"],   errors="coerce")
df["일강수량(mm)"]   = pd.to_numeric(df["일강수량(mm)"],   errors="coerce")
df["평균 풍속(m/s)"] = pd.to_numeric(df["평균 풍속(m/s)"], errors="coerce")
df["ar"]            = pd.to_numeric(df["ar"],            errors="coerce")

df = df.dropna(subset=["occu_date", "평균기온(°C)", "일강수량(mm)", "평균 풍속(m/s)", "ar"])

df["월"] = df["occu_date"].dt.month
df["연도"] = df["occu_date"].dt.year


# =========================
# 2. 가설 1
# 기온이 높고 강수량이 낮을수록 산불 발생 건수 증가
# → 월 단위 집계 + 이중축 선 그래프
# =========================

# 월별 집계 (전체 연도 합산)
monthly = df.groupby("월").agg(
    산불건수=("occu_date", "count"),
    평균기온=("평균기온(°C)", "mean"),
    평균강수량=("일강수량(mm)", "mean"),
    평균풍속=("평균 풍속(m/s)", "mean")
).reset_index()

print("===== 가설 1: 월별 집계 =====")
print(monthly)

# 상관관계 (월 단위)
corr = monthly[["산불건수", "평균기온", "평균강수량", "평균풍속"]].corr()
print("\n===== 가설 1: 상관관계 (월 단위) =====")
print(corr["산불건수"])

color_fire = "#E74C3C"
color_temp = "#3498DB"
color_rain = "#2ECC71"

# ----- 그래프 1: 이중축 통합 (기온 + 반전강수량 + 산불건수 막대) -----
fig, ax1 = plt.subplots(figsize=(11, 5))

# 산불건수 막대
ax1.bar(monthly["월"], monthly["산불건수"], color=color_fire, alpha=0.35, label="산불 발생 건수")
ax1.set_xlabel("월")
ax1.set_ylabel("산불 발생 건수", color=color_fire)
ax1.tick_params(axis="y", labelcolor=color_fire)
ax1.set_xticks(range(1, 13))
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x)}월"))

# 오른쪽 축: 기온 + 반전강수량
ax2 = ax1.twinx()
ax2.plot(monthly["월"], monthly["평균기온"],
         color=color_temp, marker="o", linewidth=2.5, label="평균기온(°C)")
ax2.plot(monthly["월"], -monthly["평균강수량"],   # 강수량 반전 → 낮을수록 위로
         color=color_rain, marker="s", linewidth=2.5, linestyle="--", label="강수량 반전(-mm)")
ax2.set_ylabel("평균기온(°C) / 강수량 반전(-mm)", color="gray")
ax2.tick_params(axis="y", labelcolor="gray")

# 범례 통합
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

plt.title("월별 기온·강수량(반전)과 산불 발생 건수 (2020~2024)\n※ 강수량 반전: 선이 위로 올라갈수록 강수량 적음")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("가설1_통합그래프.png", dpi=150)
plt.show()

# ----- 그래프 2: 상관계수 히트맵 -----
fig, ax = plt.subplots(figsize=(6, 5))

corr_display = monthly[["산불건수", "평균기온", "평균강수량", "평균풍속"]].corr()
corr_display.index   = ["산불건수", "평균기온(°C)", "강수량(mm)", "풍속(m/s)"]
corr_display.columns = ["산불건수", "평균기온(°C)", "강수량(mm)", "풍속(m/s)"]

sns.heatmap(
    corr_display,
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    center=0,
    vmin=-1, vmax=1,
    linewidths=0.5,
    ax=ax
)
ax.set_title("가설 1: 기상요인 × 산불건수 상관계수 히트맵\n(월 단위, 2020~2024)")
plt.tight_layout()
plt.savefig("가설1_상관계수히트맵.png", dpi=150)
plt.show()


# =========================
# 3. 가설 2
# 봄철(2~4월)은 다른 계절보다 산불 발생 건수와 피해면적이 크다
# =========================

def season_group(month):
    return "봄철(2~4월)" if month in [2, 3, 4] else "그 외 계절"

df["계절구분"] = df["월"].apply(season_group)

season_count = df.groupby("계절구분").size().reset_index(name="산불발생건수")
season_area  = df.groupby("계절구분")["ar"].sum().reset_index(name="피해면적합계")

print("\n===== 가설 2: 계절별 산불 발생 건수 =====")
print(season_count)
print("\n===== 가설 2: 계절별 피해면적 합계 =====")
print(season_area)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=season_count, x="계절구분", y="산불발생건수",
            palette=["#E74C3C", "#95A5A6"], ax=axes[0])
axes[0].set_title("봄철 vs 그 외 계절 산불 발생 건수")
axes[0].set_xlabel("계절 구분")
axes[0].set_ylabel("산불 발생 건수")
axes[0].grid(axis="y", alpha=0.4)

sns.barplot(data=season_area, x="계절구분", y="피해면적합계",
            palette=["#E74C3C", "#95A5A6"], ax=axes[1])
axes[1].set_title("봄철 vs 그 외 계절 피해면적 합계")
axes[1].set_xlabel("계절 구분")
axes[1].set_ylabel("피해면적 합계")
axes[1].grid(axis="y", alpha=0.4)

plt.tight_layout()
plt.savefig("가설2_봄철비교.png", dpi=150)
plt.show()


# =========================
# 4. 월별 추가 분석
# =========================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

monthly_count = df.groupby("월").size().reset_index(name="산불발생건수")
monthly_area  = df.groupby("월")["ar"].sum().reset_index(name="피해면적합계")

# 봄철 강조용 색상
colors = ["#E74C3C" if m in [2, 3, 4] else "#AEB6BF" for m in monthly_count["월"]]

axes[0].bar(monthly_count["월"], monthly_count["산불발생건수"], color=colors)
axes[0].set_title("월별 산불 발생 건수 (빨강=봄철)")
axes[0].set_xlabel("월")
axes[0].set_ylabel("산불 발생 건수")
axes[0].set_xticks(range(1, 13))
axes[0].grid(axis="y", alpha=0.4)

colors_area = ["#E74C3C" if m in [2, 3, 4] else "#AEB6BF" for m in monthly_area["월"]]
axes[1].bar(monthly_area["월"], monthly_area["피해면적합계"], color=colors_area)
axes[1].set_title("월별 피해면적 합계 (빨강=봄철)")
axes[1].set_xlabel("월")
axes[1].set_ylabel("피해면적 합계")
axes[1].set_xticks(range(1, 13))
axes[1].grid(axis="y", alpha=0.4)

plt.tight_layout()
plt.savefig("월별_추가분석.png", dpi=150)
plt.show()


# =========================
# 5. 검증 출력
# =========================
print("\n===== 검증: 전체 데이터 크기 =====")
print(df.shape)

print("\n===== 기상값 결측치 =====")
print(df[["평균기온(°C)", "일강수량(mm)", "평균 풍속(m/s)"]].isnull().sum())

print("\n===== 기상관측소 거리 요약 =====")
print(df["기상지점거리_km"].describe())
print(f"50km 초과: {(df['기상지점거리_km'] > 50).sum()}건")
print(f"100km 초과: {(df['기상지점거리_km'] > 100).sum()}건")

print("\n분석 완료")