import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 


df = pd.read_csv('기상청(2021-5~2026-5).csv',
                 header=0,                 
                 encoding='cp949'         
                                   )   
df2 = pd.read_excel('산림청(2016~2025).xls',
                    header=2
                    )  
# 2. 2021~2025년 산불만 필터링
filtered_df = df2[
    (df2['발생일시_년'] >= 2021) &
    (df2['발생일시_년'] <= 2025)
].copy()

start_str = (
    filtered_df['발생일시_년'].astype(str) + '-' +
    filtered_df['발생일시_월'].astype(str).str.zfill(2) + '-' +
    filtered_df['발생일시_일'].astype(str).str.zfill(2) + ' ' +
    filtered_df['발생일시_시간'].astype(str)
)


end_str = (
    filtered_df['진화종료시간_년'].astype(str) + '-' +
    filtered_df['진화종료시간_월'].astype(str).str.zfill(2) + '-' +
    filtered_df['진화종료시간_일'].astype(str).str.zfill(2) + ' ' +
    filtered_df['진화종료시간_시간'].astype(str)
)


filtered_df['발생시점'] = pd.to_datetime(start_str, errors='coerce')
filtered_df['진화시점'] = pd.to_datetime(end_str, errors='coerce')

filtered_df['발생일자'] = filtered_df['발생시점'].dt.date


filtered_df['진화소요시간_분'] = (
    filtered_df['진화시점'] - filtered_df['발생시점']
).dt.total_seconds() / 60

filtered_df['진화소요시간_시간'] = filtered_df['진화소요시간_분'] / 60

filtered_df['피해면적_ha'] = pd.to_numeric(
    filtered_df['피해면적_합계'],
    errors='coerce'
)


filtered_df['시군구_정제'] = (
    filtered_df['발생장소_시군구']
    .astype(str)
    .str.strip()
    .str.replace(" ", "", regex=False)
)


filtered_df['시군구_정제'] = filtered_df['시군구_정제'].replace({
    'nan': pd.NA,
    '': pd.NA,
    '미상': pd.NA
})


check_cols = [
    '발생시점',
    '진화시점',
    '발생일자',
    '발생장소_시군구',
    '시군구_정제',
    '피해면적_ha',
    '진화소요시간_분'
]

print("결측치 개수")
print(filtered_df[check_cols].isna().sum())

filtered_df['진화시간_결측여부'] = filtered_df['진화소요시간_분'].isna()


filtered_df = filtered_df.dropna(
    subset=['발생시점', '시군구_정제', '피해면적_ha']
).copy()


filtered_df = filtered_df[
    (filtered_df['진화소요시간_분'].isna()) |
    (filtered_df['진화소요시간_분'] >= 0)
].copy()

# 14. 최종 결측치 확인
print("결측치 처리 후")
print(filtered_df[check_cols].isna().sum())

print(f"최종 데이터 개수: {len(filtered_df)}개")

print(
    filtered_df[
        ['발생일자', '시군구_정제', '피해면적_ha', '진화소요시간_분', '진화시간_결측여부']
    ].head()
)

print(df2.isnull().sum())



print(df.info())

