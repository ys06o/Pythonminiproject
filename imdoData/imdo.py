import pandas as pd
import datetime
df = pd.DataFrame()
end_dt = 0
start_dt = 0

# 산불발생이력 데이터에서 시작날짜와 시간, 
# 종료년, 달, 일, 시간 데이터로 진화시간_분 계산후 파생변수 생성 

df['start_dt'] = pd.to_datetime(
    df['occu_date'].astype(str) + df['occu_tm'].astype(str).str.zfill(4), 
    format='%Y%m%d%H%M')

df['end_dt'] = pd.to_datetime(
    df['end_year'].astype(str) + df['end_mt'].astype(str).str.zfill(2) + 
    df['end_de'].astype(str).str.zfill(2) + df['end_tm'].astype(str).str.zfill(4), 
    format='%Y%m%d%H%M')

df['진화시간_분'] = (df['end_dt'] - df['start_dt']).dt.total_seconds() / 60


