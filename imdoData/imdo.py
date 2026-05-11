import pandas as pd
from dbfread import DBF
import os
from pyproj import Transformer
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tqdm import tqdm  # 진행바 표시용: pip install tqdm

# 1. 파일 통합 설정
folder_path = 'imdoData/Data' 
all_data = []

# 2. DBF 파일 순회 및 통합
print("데이터 불러오기 시작...")
for file_name in os.listdir(folder_path):
    if file_name.endswith('.dbf'):
        file_path = os.path.join(folder_path, file_name)
        try:
            table = DBF(file_path, encoding='cp949')
            df = pd.DataFrame(iter(table))
            df['SOURCE_FILE'] = file_name # 원본 파일명 저장
            all_data.append(df)
        except Exception as e:
            print(f"오류 발생 ({file_name}): {e}")

if not all_data:
    print("불러올 데이터가 없습니다. 경로를 확인하세요.")
    exit()

final_df = pd.concat(all_data, ignore_index=True)
print(f"통합 완료: 총 {len(final_df)}행")

# 3. 좌표 변환 (TM중부 5179 -> 위경도 4326)
transformer = Transformer.from_crs("EPSG:5179", "EPSG:4326", always_xy=True)

def convert_to_wgs84(row):
    try:
        lon, lat = transformer.transform(row['RBP_X'], row['RBP_Y'])
        return pd.Series([lat, lon])
    except:
        return pd.Series([None, None])

print("좌표 변환 중...")
final_df[['LAT', 'LON']] = final_df.apply(convert_to_wgs84, axis=1)

# 4. 데이터 정제 및 칼럼명 한글화
final_df['SOURCE_FILE'] = final_df['SOURCE_FILE'].str.replace('.dbf', '', regex=False)

column_names = {
    'SOURCE_FILE': '지역',
    'FRRD_NM': '임도명',
    'FRRD_FCLTD': '시설거리(km)',
    'FRRD_ESTBL': '개설연도',
    'LAT': '위도',
    'LON': '경도'
}
final_df = final_df.rename(columns=column_names)

# 데이터 타입 정리
final_df['개설연도'] = pd.to_numeric(final_df['개설연도'], errors='coerce').fillna(0).astype(int)
final_df['시설거리(km)'] = pd.to_numeric(final_df['시설거리(km)'], errors='coerce')

# 5. 주소 변환 (역지오코딩) - 읍/면 추출 중심
print("주소 변환을 시작합니다. (약 1시간 소요 예정)")

geolocator = Nominatim(user_agent="south_korea_forest_fire_project_v2")
# 1초 간격으로 요청하도록 설정 (OpenStreetMap 정책 준수)
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1.1)

# 진행 상황 확인을 위해 tqdm 적용
tqdm.pandas()

def get_detailed_addr(lat, lon):
    try:
        location = reverse((lat, lon), language='ko')
        if location:
            addr = location.raw.get('address', {})
            # 읍/면 정보를 우선적으로 추출
            town = addr.get('town', addr.get('village', addr.get('suburb', addr.get('neighbourhood', ''))))
            full_addr = location.address
            return pd.Series([full_addr, town])
    except:
        return pd.Series([None, None])

# 실제 변환 수행 (LAT, LON -> 상세주소, 읍면동)
final_df[['상세주소', '읍면동']] = final_df.progress_apply(
    lambda row: get_detailed_addr(row['위도'], row['경도']), axis=1
)

# 6. 최종 CSV 저장
output_file = '전국_임도망_상세주소_통합본.csv'
final_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n--- 모든 작업 완료 ---")
print(f"최종 저장된 파일: {output_file}")