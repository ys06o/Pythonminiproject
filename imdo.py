import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  #serborn
import re

df_fire = pd.read_csv('산불_기상_통합본.csv',encoding='utf-8')
df_fire['진화시간_분'] = df_fire['진화시간_분'].fillna(0).astype(int)
df_fire.info()
# 해당 년도에 발생한 전체 산불 갯수 및 대형산불 갯수

df_fire['대형산불'] = df_fire['피해면적'] >= 1
df_fire2020 = df_fire[df_fire['발생연도']== 2020]
df_fire2021 = df_fire[df_fire['발생연도']== 2021]
df_fire2022 = df_fire[df_fire['발생연도']== 2022]
df_fire2023 = df_fire[df_fire['발생연도']== 2023]
df_fire2024 = df_fire[df_fire['발생연도']== 2024]
print(df_fire2021[df_fire2021['대형산불']==True]['피해면적'].mean())
# 막대 그래프 .bar(x축, y축, width= 굴기, label='항목명', color='색상)
categories = ['2020년', '2021년', '2022년', '2023년', '2024년'] 
fire = [df_fire2020['발생연도'].count(), df_fire2021['발생연도'].count(), df_fire2022['발생연도'].count(), df_fire2023['발생연도'].count(), df_fire2024['발생연도'].count()]
bigfire = [df_fire2020[df_fire2020['대형산불']==True]['대형산불'].count(), df_fire2021[df_fire2021['대형산불']==True]['대형산불'].count(), df_fire2022[df_fire2022['대형산불']==True]['대형산불'].count(), df_fire2023[df_fire2023['대형산불']==True]['대형산불'].count(), df_fire2024[df_fire2024['대형산불']==True]['대형산불'].count()]
# 막대 곂치지 않게 표시
import numpy as np
x = np.arange(len(categories)) 

plt.bar(x - 0.2, fire, width=0.4, label='전체 산불 횟수', color='blue')
plt.bar(x + 0.2, bigfire, width=0.4, label='대형 산불 횟수', color='red')
plt.title('연도별 화재 횟수 대비 대형산불 횟수')
plt.xlabel('발생 연도')
plt.ylabel('화재 횟수')
plt.legend()
plt.grid(axis='y') # 눈금선 (y축만)
plt.xticks(x, categories) # 위치 순으로 라벨 지정
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