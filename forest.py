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

# 하나의 그래프 안에 피해 면적 막대와 발생 빈도 막대를 함께 표시
x = range(len(frtp_통계))
bar_width = 0.4

plt.figure(figsize=(10, 6))

plt.bar(
    [i - bar_width / 2 for i in x],
    frtp_통계['ar'],
    width=bar_width,
    label='피해 면적 합계'
)

plt.bar(
    [i + bar_width / 2 for i in x],
    frtp_통계['AGCLS_CD'],
    width=bar_width,
    label='발생 빈도'
)

plt.xticks(x, frtp_통계['수종'])
plt.title('수종별 산불 피해 면적과 발생 빈도')
plt.xlabel('수종')
plt.ylabel('피해 면적 / 발생 빈도')
plt.legend()
plt.tight_layout()
plt.show()



