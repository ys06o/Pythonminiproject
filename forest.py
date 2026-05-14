import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 
import math as m


#------------------------------------------------------------------
# 임상도 파일
# 서울
df_강1= pd.read_csv('임상도/강원특별자치도1.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_강2= pd.read_csv('임상도/강원특별자치도2.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 
df_강원특별자치도 = pd.concat( [df_강1 , df_강2 ], ignore_index=True )

df_경기도= pd.read_csv('임상도/경기도.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_경상남도= pd.read_csv('임상도/경상남도.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_경상북도1= pd.read_csv('임상도/경상북도1.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_경상북도2= pd.read_csv('임상도/경상북도2.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_경상북도 = pd.concat( [df_경상북도1 , df_경상북도2 ], ignore_index=True )

df_광주광역시= pd.read_csv('임상도/광주광역시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_대구광역시= pd.read_csv('임상도/대구광역시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_대전광역시= pd.read_csv('임상도/대전광역시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_부산광역시= pd.read_csv('임상도/부산광역시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_서울특별시= pd.read_csv('임상도/서울특별시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_세종특별자치시= pd.read_csv('임상도/세종특별자치시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_울산광역시= pd.read_csv('임상도/울산광역시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_인천광역시= pd.read_csv('임상도/인천광역시.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_전라남도= pd.read_csv('임상도/전라남도.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_전북특별자치도= pd.read_csv('임상도/전북특별자치도.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_충청남도= pd.read_csv('임상도/충청남도.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_충청북도= pd.read_csv('임상도/충청북도.csv',
                 header=0,
                 usecols=['갱신년도','FRTP_CD','AGCLS_CD','DNST_CD','latitude','longitude','location'],                 
                 encoding='utf-8-sig'  # CSV 파일이 UTF-8 BOM 형식이라 utf-8-sig로 읽어야 함
                                   ) 

df_산불 = pd.read_csv('산불발생이력.csv',
                    header=0,
                    usecols=['x','y','occu_year','ar']
                    )

# -----------------------------------------------------------------

# 갱신년도코드 - 갱신년도 
# 임상코드(FRTP_CD) - 침엽수, 활엽수
# 영급코드(AGCLS_CD) - 평균적이 나이대
# 밀도코드(DNST_CD) - 산림의 나무 밀도

df_전지역 = pd.concat( [df_강원특별자치도 , df_경기도, df_경상남도, df_경상북도, df_광주광역시, 
                       df_대구광역시, df_대전광역시, df_부산광역시,  df_서울특별시, df_세종특별자치시, 
                       df_울산광역시 , df_인천광역시 , df_전라남도 , df_전북특별자치도 , df_충청남도 ,df_충청북도], ignore_index=True )

newDf = df_전지역.dropna( axis=0 )
a = newDf['갱신년도'] > 2019
b = newDf['갱신년도'] < 2025

new_전지역 = newDf[a & b]

c = df_산불['occu_year'] > 2019
d = df_산불['occu_year'] < 2025

산불05 = df_산불[c & d]

산림_좌표 = new_전지역.copy()
산불_좌표 = 산불05.copy()

산림_좌표['위도_소수3'] = 산림_좌표['latitude'].round(3)
산림_좌표['경도_소수3'] = 산림_좌표['longitude'].round(3)

산불_좌표['위도_소수3'] = 산불_좌표['y'].round(3)
산불_좌표['경도_소수3'] = 산불_좌표['x'].round(3)



같은_좌표_행 = pd.merge(
    산림_좌표,
    산불_좌표,
    on=['위도_소수3', '경도_소수3'],
    how='inner'
)

# 필요한 열만 추출
일치_결과 = 같은_좌표_행[
    ['FRTP_CD', 'AGCLS_CD', 'DNST_CD', 'ar']
]

# 수종/수령 분석에서도 피해면적(ar)이 0인 산불은 1로 전처리
일치_결과['ar'] = pd.to_numeric(일치_결과['ar'], errors='coerce')
일치_결과.loc[일치_결과['ar'] == 0, 'ar'] = 1

# 피해 면적(ar)이 10 이하인 데이터만 분석에 사용
일치_결과 = 일치_결과[일치_결과['ar'] <= 10]

print(일치_결과.head())

# 수종 코드별 피해 면적 합계와 발생 빈도 구하기
# day15, day16 예제처럼 groupby + agg + reset_index 흐름으로 작성
frtp_통계 = 일치_결과.groupby('FRTP_CD').agg({
    'ar': 'sum',
    'AGCLS_CD': 'count'
}).reset_index()

# 피해 면적을 발생 빈도로 나눈 값을 퍼센트로 계산
frtp_통계['피해면적_빈도_비율'] = (frtp_통계['ar'] / frtp_통계['AGCLS_CD']) * 100

# FRTP_CD 숫자 코드를 한글 이름으로 변경
frtp_이름 = {
    1: '침엽수',
    2: '활엽수',
    3: '혼효림'
}
frtp_통계['수종'] = frtp_통계['FRTP_CD'].map(frtp_이름)

print(frtp_통계)
print(frtp_통계[['수종', '피해면적_빈도_비율']])

# 피해 면적은 막대그래프, 발생 빈도는 선그래프로 표시
# 두 값을 같은 y축 기준으로 표시
x = range(len(frtp_통계))
bar_width = 0.4

fig, ax1 = plt.subplots(figsize=(7, 6))

ax1.bar(
    x,
    frtp_통계['ar'],
    width=bar_width,
    color='#7fb069',
    label='피해 면적 합계'
)
ax1.set_xlabel('수종')
ax1.set_ylabel('피해 면적 합계 / 발생 빈도')
ax1.set_xticks(x)
ax1.set_xticklabels(frtp_통계['수종'])

ax1.plot(
    x,
    frtp_통계['AGCLS_CD'],
    color='#d95f02',
    marker='o',
    linewidth=2,
    label='발생 빈도'
)

plt.title('수종별 산불 피해 면적과 발생 빈도')
ax1.legend(loc='upper right')
plt.tight_layout()
plt.show()

# 수령(영급) 코드별 피해 면적 합계와 발생 빈도 구하기
# 수종 분석과 같은 일치_결과 데이터를 사용해서 비교 기준을 맞춤
agcls_통계 = 일치_결과.groupby('AGCLS_CD').agg({
    'ar': 'sum',
    'FRTP_CD': 'count'
}).reset_index()

# 그래프에서 이해하기 쉽도록 발생 빈도 컬럼 이름 변경
agcls_통계 = agcls_통계.rename(columns={'FRTP_CD': '발생빈도'})

# 피해 면적을 발생 빈도로 나눈 값을 퍼센트로 계산
agcls_통계['피해면적_빈도_비율'] = (agcls_통계['ar'] / agcls_통계['발생빈도']) * 100

# AGCLS_CD 숫자 코드를 실제 수령 구간 이름으로 변경
agcls_이름 = {
    1: '1~10년생',
    2: '11~20년생',
    3: '21~30년생',
    4: '31~40년생',
    5: '41~50년생',
    6: '51~60년생',
    7: '61~70년생',
    8: '71~80년생',
    9: '81년생 이상'
}
agcls_통계['수령'] = agcls_통계['AGCLS_CD'].map(agcls_이름)

print(agcls_통계)
print(agcls_통계[['수령', '피해면적_빈도_비율']])

# 피해 면적은 막대그래프, 발생 빈도는 선그래프로 표시
# 수령은 순서가 있는 값이라 선그래프로 변화 흐름을 보기 좋게 표현
# 두 값을 같은 y축 기준으로 표시
x = range(len(agcls_통계))
bar_width = 0.4

fig, ax1 = plt.subplots(figsize=(9, 6))

ax1.bar(
    x,
    agcls_통계['ar'],
    width=bar_width,
    color='#7fb069',
    label='피해 면적 합계'
)
ax1.set_xlabel('수령')
ax1.set_ylabel('피해 면적 합계 / 발생 빈도')
ax1.set_xticks(x)
ax1.set_xticklabels(agcls_통계['수령'], rotation=30)

ax1.plot(
    x,
    agcls_통계['발생빈도'],
    color='#d95f02',
    marker='o',
    linewidth=2,
    label='발생 빈도'
)

plt.title('수령별 산불 피해 면적과 발생 빈도')
ax1.legend(loc='upper right')
plt.tight_layout()
plt.show()


# 시작
# 산불_기상_매핑완료_2020_2024.csv를 사용해서 유사 기상조건별 DNST_CD 피해면적 비교
df_산불기상 = pd.read_csv('산불_기상_매핑완료_2020_2024.csv', encoding='utf-8-sig')

# 분석에 사용할 기상 컬럼을 숫자형으로 변환
df_산불기상['평균기온(°C)'] = pd.to_numeric(df_산불기상['평균기온(°C)'], errors='coerce')
df_산불기상['평균 풍속(m/s)'] = pd.to_numeric(df_산불기상['평균 풍속(m/s)'], errors='coerce')
df_산불기상['일강수량(mm)'] = pd.to_numeric(df_산불기상['일강수량(mm)'], errors='coerce')
df_산불기상['ar'] = pd.to_numeric(df_산불기상['ar'], errors='coerce')

# 피해면적(ar)이 0인 산불은 그래프에서 보이지 않으므로 1로 전처리
df_산불기상.loc[df_산불기상['ar'] == 0, 'ar'] = 1

# 결측치 제거
df_산불기상 = df_산불기상.dropna(
    subset=['평균기온(°C)', '평균 풍속(m/s)', '일강수량(mm)', 'x', 'y', 'ar']
)

# 기존 분석 조건과 맞추기 위해 피해 면적이 10 이하인 산불만 사용
df_산불기상 = df_산불기상[df_산불기상['ar'] <= 10]

# pd.cut으로 기상조건을 구간화
df_산불기상['기온구간'] = pd.cut(
    df_산불기상['평균기온(°C)'],
    bins=[-50, 10, 25, 50],
    labels=['저온', '보통기온', '고온']
)

df_산불기상['풍속구간'] = pd.cut(
    df_산불기상['평균 풍속(m/s)'],
    bins=[-1, 2, 5, 100],
    labels=['약풍', '보통풍', '강풍']
)

df_산불기상['강수구간'] = pd.cut(
    df_산불기상['일강수량(mm)'],
    bins=[-1, 0, 5, 1000],
    labels=['무강수', '적은강수', '많은강수']
)

# 기온, 풍속, 강수량 구간을 하나의 유사 기상조건 이름으로 합치기
df_산불기상['기상조건'] = (
    df_산불기상['기온구간'].astype(str) + '_' +
    df_산불기상['풍속구간'].astype(str) + '_' +
    df_산불기상['강수구간'].astype(str)
)

# 산불이 많이 발생한 상위 5개 기상조건 확인
기상조건_발생빈도 = df_산불기상['기상조건'].value_counts().head(5)
print('상위 5개 유사 기상조건별 산불 발생 빈도')
print(기상조건_발생빈도)

# 산불기상 데이터에도 임상도와 같은 좌표 기준 컬럼 생성
산불기상_좌표 = df_산불기상.copy()
산불기상_좌표['위도_소수3'] = 산불기상_좌표['y'].round(3)
산불기상_좌표['경도_소수3'] = 산불기상_좌표['x'].round(3)

# 임상도 좌표와 산불기상 좌표를 병합해서 DNST_CD를 붙이기
산림_산불기상_병합 = pd.merge(
    산림_좌표,
    산불기상_좌표,
    on=['위도_소수3', '경도_소수3'],
    how='inner'
)

# 상위 5개 기상조건만 그래프 분석에 사용
상위_기상조건 = 기상조건_발생빈도.index
상위_기상조건_데이터 = 산림_산불기상_병합[
    산림_산불기상_병합['기상조건'].isin(상위_기상조건)
]

# 유사 기상조건과 밀도코드(DNST_CD)에 따른 피해면적 합계 비교
밀도_피해면적 = 상위_기상조건_데이터.groupby(['기상조건', 'DNST_CD']).agg({
    'ar': 'sum'
}).reset_index()

print('유사 기상조건 + 밀도코드별 피해면적 합계')
print(밀도_피해면적)

# 보통 밀도(B)는 분석 데이터에 없거나 비교 대상에서 제외하므로 A, C만 사용
밀도_피해면적 = 밀도_피해면적[밀도_피해면적['DNST_CD'].isin(['A', 'C'])].copy()

# 밀도코드 A, C를 그래프에 표시할 이름으로 변경
밀도_이름 = {
    'A': '낮은 밀도',
    'C': '높은 밀도'
}
밀도_피해면적['밀도이름'] = 밀도_피해면적['DNST_CD'].map(밀도_이름)

# 유사 기상조건과 산림 밀도 조합별 피해면적을 히트맵으로 표시
# 색이 진할수록 해당 조합의 피해면적 합계가 큼
밀도_피해면적_히트맵 = 밀도_피해면적.pivot_table(
    index='기상조건',
    columns='밀도이름',
    values='ar',
    aggfunc='sum',
    fill_value=0
)

밀도_피해면적_히트맵 = 밀도_피해면적_히트맵.reindex(columns=['낮은 밀도', '높은 밀도'])

plt.figure(figsize=(8, 6))
sns.heatmap(
    밀도_피해면적_히트맵,
    annot=True,
    fmt='.0f',
    cmap='YlGnBu',
    linewidths=0.5
)
plt.title('유사 기상조건별 산림 밀도에 따른 피해면적 비교')
plt.xlabel('산림 밀도')
plt.ylabel('유사 기상조건')
plt.tight_layout()
plt.show()

# 산불 발생 지점 기준으로 낮은 밀도(A)와 높은 밀도(C)의 비율 확인
밀도_발생비율 = 상위_기상조건_데이터[
    상위_기상조건_데이터['DNST_CD'].isin(['A', 'C'])
]['DNST_CD'].value_counts().reindex(['A', 'C'], fill_value=0)

밀도_발생비율.index = 밀도_발생비율.index.map(밀도_이름)

plt.figure(figsize=(7, 7))
plt.pie(
    밀도_발생비율,
    labels=밀도_발생비율.index,
    autopct='%.1f%%',
    startangle=90,
    colors=['#7fb069', '#2d6a4f']
)
plt.title('산불 발생 시 산림 밀도 비율')
plt.tight_layout()
plt.show()
# 끝


