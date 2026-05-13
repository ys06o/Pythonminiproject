import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import koreanfont

# =========================
# 1. 데이터 불러오기
# =========================
df = pd.read_csv("산불_기상_매핑완료_2020_2024.csv", encoding="utf-8-sig")

df["occu_date"]      = pd.to_datetime(df["occu_date"], errors="coerce")
df["일시"]           = pd.to_datetime(df["일시"],      errors="coerce")
df["평균기온(°C)"]   = pd.to_numeric(df["평균기온(°C)"],   errors="coerce")
df["일강수량(mm)"]   = pd.to_numeric(df["일강수량(mm)"],   errors="coerce")
df["평균 풍속(m/s)"] = pd.to_numeric(df["평균 풍속(m/s)"], errors="coerce")
df["ar"]             = pd.to_numeric(df["ar"],            errors="coerce")

df = df.dropna(subset=["occu_date", "일시", "평균기온(°C)", "일강수량(mm)", "평균 풍속(m/s)", "ar"])

df["월"] = df["occu_date"].dt.month
df["연도"] = df["occu_date"].dt.year


# =========================
# 2. 가설 1
# 기온이 높고 일강수량이 낮을수록 산불 발생 건수는 증가할 것이다.
#
# [핵심] 기상값은 날짜+지점 기준으로 중복 제거 후 월별 집계
#        산불 건수는 별도로 카운트 → 월 기준 merge
# =========================

# --- 기상 데이터: 날짜+기상지점 중복 제거 후 월별 집계 ---
weather_daily = df.drop_duplicates(subset=["일시", "가까운_기상지점명"])
weather_daily = weather_daily.copy()
weather_daily["월"] = weather_daily["일시"].dt.month

weather_monthly = weather_daily.groupby("월").agg(
    평균기온=("평균기온(°C)", "mean"),
    강수량합계=("일강수량(mm)", "sum"),   # 일강수량 월 합계 (중복 제거 후)
    평균풍속=("평균 풍속(m/s)", "mean")
).reset_index()

# --- 산불 건수: 월별 카운트 ---
fire_monthly = df.groupby("월").size().reset_index(name="산불건수")

# --- merge ---
monthly = fire_monthly.merge(weather_monthly, on="월", how="inner")

print("===== 가설 1: 월별 집계 =====")
print(monthly)

# 상관관계
corr = monthly[["산불건수", "평균기온", "강수량합계", "평균풍속"]].corr()
print("\n===== 가설 1: 상관관계 (월 단위) =====")
print(corr["산불건수"])

color_fire = "#E74C3C"
color_temp = "#3498DB"
color_rain = "#2ECC71"

# ----- 그래프 1: 이중축 통합 (기온 + 반전강수량 + 산불건수 막대) -----
fig, ax1 = plt.subplots(figsize=(11, 5))

ax1.bar(monthly["월"], monthly["산불건수"], color=color_fire, alpha=0.35, label="산불 발생 건수")
ax1.set_xlabel("월")
ax1.set_ylabel("산불 발생 건수", color=color_fire)
ax1.tick_params(axis="y", labelcolor=color_fire)
ax1.set_xticks(range(1, 13))
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x)}월"))

ax2 = ax1.twinx()
ax2.plot(monthly["월"], monthly["평균기온"],
         color=color_temp, marker="o", linewidth=2.5, label="평균기온(°C)")
ax2.plot(monthly["월"], -monthly["강수량합계"],  # 반전: 낮을수록 위로
         color=color_rain, marker="s", linewidth=2.5, linestyle="--", label="강수량 반전(-mm)")
ax2.set_ylabel("평균기온(°C) / 강수량 반전(-mm)", color="gray")
ax2.tick_params(axis="y", labelcolor="gray")

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

corr_display = monthly[["산불건수", "평균기온", "강수량합계", "평균풍속"]].corr()
corr_display.index   = ["산불건수", "평균기온(°C)", "강수량합계(mm)", "풍속(m/s)"]
corr_display.columns = ["산불건수", "평균기온(°C)", "강수량합계(mm)", "풍속(m/s)"]

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

df_imdo = pd.read_csv('imdoData/Data/전국_임도망_정제본.csv',encoding='utf-8')
df_imdo.info()

df_fire['시군구_clean'] = df_fire['시군구'].str.replace(r'(시|군|구)$', '', regex=True).str.strip()
def extract_sigungu(addr):
    if pd.isna(addr): return ""
    parts = str(addr).split(',')
    for part in parts:
        part = part.strip()
        if '시' in part or '군' in part or '구' in part:
            return re.sub(r'(시|군|구)$', '', part).strip()
    return ""

df_imdo['시군구_clean'] = df_imdo['상세주소'].apply(extract_sigungu)

def get_road_length_at_time(fire_row):
    # 해당 시군구의 임도 중, 산불 발생연도와 같거나 그 이전에 개설된 것만 필터링
    target_roads = df_imdo[
        (df_imdo['시군구_clean'] == fire_row['시군구_clean']) & 
        (df_imdo['개설연도'] <= fire_row['발생연도'])
    ]
    return target_roads['시설거리(km)'].sum()

# 4. 대형 산불 데이터만 추출하여 분석 진행 (피해면적 1ha 이상)
df_big_fire = df_fire[df_fire['피해면적'] >= 0].copy()

# 각 대형 산불 행에 대해 당시 임도 길이 계산하여 추가
df_big_fire['당시_임도길이'] = df_big_fire.apply(get_road_length_at_time, axis=1)

# 5. 결과 확인
print("--- 대형 산불 당시 지역별 임도 보유 현황 ---")
print(df_big_fire[['발생연도', '시군구', '피해면적', '당시_임도길이']])

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_big_fire, x='당시_임도길이', y='피해면적',hue='피해면적', size='피해면적', palette='flare', alpha=0.6, sizes=(200, 1000))
plt.title('대형 산불 피해 규모와 당시 임도 보유량의 관계')
plt.xlabel('산불 당시 해당 지역 임도 총 길이 (km)')
plt.ylabel('피해 면적 (ha)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_big_fire, 
    x='당시_임도길이', 
    y='진화시간_분', 
    hue='진화시간_분', 
    size='진화시간_분', 
    palette='crest', 
    sizes=(100, 1000), 
    alpha=0.7
)
plt.title('산불 당시 임도 보유량과 진화 시간의 관계')
plt.xlabel('산불 당시 해당 지역 임도 총 길이 (km)')
plt.ylabel('진화 시간 (분)')
plt.grid(True)
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