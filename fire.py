import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 


df = pd.read_csv('산불발생이력.csv',encoding='utf-8')


print(df.head()) #상위 5개행 불러오기
print(df.info()) #정보 불러오기
print(df.isnull().sum()) #결측치 확인

df.dropna(inplace=True)
print(df.isnull().sum()) #결측치 있는 행 삭제



import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from scipy.spatial import distance
import seaborn as sns
import matplotlib.pyplot as plt
import time

# 1. 데이터 로드
df_fire = pd.read_csv('산불발생이력.csv', encoding='utf-8')
df_weather = pd.read_csv('기상청_일단위_주소통합.csv', encoding='utf-8')

# 날짜 형식 정리
df_fire['occu_date'] = pd.to_datetime(df_fire['occu_date'], format='%Y%m%d')
df_weather['일시'] = pd.to_datetime(df_weather['일시'])

# 2. [지오코딩] 지점 주소를 좌표로 변환 (중요!)
# 502개를 매번 변환하면 느리므로, 고유 주소만 뽑아서 좌표를 찾습니다.
unique_addresses = df_weather['지점주소'].dropna().unique()
geolocator = Nominatim(user_agent="my_fire_project")

print(f"총 {len(unique_addresses)}개의 지점 좌표를 찾는 중... (시간이 걸릴 수 있습니다)")
station_coords = []

for addr in unique_addresses:
    # 주소 앞의 '(산지)' 같은 특수 문구 제거
    clean_addr = addr.replace('(산지)', '').strip()
    try:
        location = geolocator.geocode(clean_addr)
        if location:
            station_coords.append({'지점주소': addr, 'lat': location.latitude, 'lon': location.longitude})
        time.sleep(0.1) # 서버 과부하 방지
    except:
        continue

df_stations = pd.DataFrame(station_coords)

# 3. [최단거리 매핑] 산불 위치와 가장 가까운 기상 지점 연결
def find_nearest(row):
    if df_stations.empty: return None
    # 유클리드 거리 계산
    dists = df_stations.apply(
        lambda s: distance.euclidean((row['y'], row['x']), (s['lat'], s['lon'])), axis=1
    )
    return df_stations.loc[dists.idxmin(), '지점주소']

print("산불 위치와 가장 가까운 관측소 매칭 중...")
df_fire['매칭주소'] = df_fire.apply(find_nearest, axis=1)

# 4. 데이터 합치기
df_total = pd.merge(df_fire, df_weather, 
                    left_on=['occu_date', '매칭주소'], 
                    right_on=['일시', '지점주소'], 
                    how='inner')

# 5. 가설 검증: 고온, 저습, 저강수 분석
# 가설 컬럼: 평균기온(°C), 평균 상대습도(%), 일강수량(mm)
analysis_cols = ['ar', '평균기온(°C)', '평균 상대습도(%)', '일강수량(mm)']
# 파일 내 실제 컬럼명과 일치하는지 확인 필수!
existing_cols = [c for c in analysis_cols if c in df_total.columns]
corr = df_total[existing_cols].corr()

print("\n--- 가설 검증 결과 (피해면적 ar과의 상관계수) ---")
print(corr['ar'])

# 6. 시각화
plt.rc('font', family='Malgun Gothic')
sns.heatmap(corr, annot=True, cmap='RdYlBu_r')
plt.title('기상 요소별 산불 상관관계')
plt.show()