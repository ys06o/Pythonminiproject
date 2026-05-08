import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 


df_1 = pd.read_csv('기상청(2021-5~2026-5).csv',
                 header=0,                 
                 encoding='cp949'         
                                   )   
df_2 = pd.read_excel('산림청(2016~2025).xls' )  
df_3 = pd.read_excel('산림청(2026).xls' )  
print(df_1)
print(df_2)
print(df_3)

