import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import numpy as np
import koreanfont

df_fire = pd.read_csv('산불_기상_통합본.csv', encoding='utf-8')
df_fire['진화시간_분'] = df_fire['진화시간_분'].fillna(0).astype(int)


df_imdo = pd.read_csv('imdoData/Data/전국_임도망_정제본.csv', encoding='utf-8')
df_fire['시군구_clean'] = df_fire['시군구'].str.replace(r'(시|군|구)$', '', regex=True).str.strip()

def extract_sigungu(addr):
    if pd.isna(addr): return ""
    parts = str(addr).split(',')
    for part in parts:
        part = part.strip()
        if any(x in part for x in ['시', '군', '구']):
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


df_fire['당시_임도길이'] = df_fire.apply(get_road_length_at_time, axis=1)


# --- 시각화 1: 연도별 화재 현황 ---
df_fire['대형산불'] = df_fire['피해면적'] >= 1
years = [2020, 2021, 2022, 2023, 2024]
fire_counts = [df_fire[df_fire['발생연도'] == y]['발생연도'].count() for y in years]
bigfire_counts = [df_fire[(df_fire['발생연도'] == y) & (df_fire['대형산불'] == True)]['발생연도'].count() for y in years]

x = np.arange(len(years)) 
plt.figure(figsize=(5, 5))
plt.bar(x - 0.2, fire_counts, width=0.4, label='전체 산불 횟수', color='blue')
plt.bar(x + 0.2, bigfire_counts, width=0.4, label='1ha이상 산불 횟수', color='red')
plt.title('연도별 화재 횟수 대비 1ha 이상 피해면적 산불 횟수')
plt.xticks(x, [f'{y}년' for y in years], fontsize=15)
plt.xlabel('발생연도')
plt.ylabel('발생횟수')
plt.legend()
plt.show()

# --- 시각화 2: 산불 산점도 ---
df_big_fire = df_fire[ df_fire['피해면적'] <= 3500 ].copy()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_big_fire, x='당시_임도길이', y='피해면적', hue='피해면적', size='피해면적', palette='flare', alpha=0.6, sizes=(200, 1000))
plt.title('산불 피해 규모와 당시 임도 보유량의 관계')
plt.grid(True)
plt.show()

# --- 시각화 3: 진화 시간 산점도 ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_big_fire, x='당시_임도길이', y='진화시간_분', hue='진화시간_분', size='진화시간_분', palette='crest', sizes=(100, 1000), alpha=0.7)
plt.title('산불 당시 임도 보유량과 진화 시간의 관계')
plt.grid(True)
plt.show()

