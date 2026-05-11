import pandas as pd
from dbfread import DBF
import os

# 1. 파일들이 있는 폴더 경로 설정
folder_path = 'imdoData/Data'  # 실제 파일이 있는 폴더명으로 수정하세요

# 2. 통합할 리스트 준비
all_data = []

# 3. 폴더 내 모든 dbf 파일 순회
for file_name in os.listdir(folder_path):
    if file_name.endswith('.dbf'):
        file_path = os.path.join(folder_path, file_name)
        
        try:
            # dbf 파일 읽기 (한글 깨짐 방지를 위해 cp949 인코딩 사용)
            table = DBF(file_path, encoding='cp949')
            df = pd.DataFrame(iter(table))
            
            # 어느 지역 데이터인지 구분하기 위해 파일명 컬럼 추가
            df['SOURCE_FILE'] = file_name
            
            all_data.append(df)
            print(f"성공: {file_name} (행 개수: {len(df)})")
            
        except Exception as e:
            print(f"오류 발생 ({file_name}): {e}")

# 4. 모든 데이터 하나로 합치기
if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    print("--- 통합 완료 ---")
    print(f"전체 데이터 행 개수: {len(final_df)}")
else:
    print("불러올 DBF 파일이 없습니다.")

# 5. 데이터 샘플 확인
print(final_df[['SOURCE_FILE', 'FRRD_NM', 'FRRD_FCLTD', 'FRRD_ESTBL']].head())

import matplotlib.pyplot as plt
import seaborn as sns

# 한글 깨짐 방지 설정 (Windows 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 1. 연도별 임도 개설 총 거리 계산
# FRRD_ESTBL이 문자열일 수 있으니 숫자로 변환 후 정렬
final_df['FRRD_ESTBL'] = pd.to_numeric(final_df['FRRD_ESTBL'], errors='coerce')
yearly_dist = final_df.groupby('FRRD_ESTBL')['FRRD_FCLTD'].sum().reset_index()

# 2. 지역별(파일별) 총 임도 거리 계산
region_dist = final_df.groupby('SOURCE_FILE')['FRRD_FCLTD'].sum().sort_values(ascending=False).reset_index()


plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_dist[yearly_dist['FRRD_ESTBL'] > 1990], x='FRRD_ESTBL', y='FRRD_FCLTD', marker='o', color='forestgreen')
plt.title('연도별 신규 임도 개설 거리 추이 (1990년 이후)')
plt.xlabel('개설 연도')
plt.ylabel('총 거리 (km)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=region_dist, x='SOURCE_FILE', y='FRRD_FCLTD', palette='viridis')
plt.title('지역별(파일명) 임도 확보 총 거리 비교')
plt.xticks(rotation=45)
plt.ylabel('총 거리 (km)')
plt.show()