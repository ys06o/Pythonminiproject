import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  #serborn

df = pd.read_csv('기상청_일단위.csv',encoding='cp949')


print(df.head()) #상위 5개행 불러오기
print(df.info()) #정보 불러오기
print(df.isnull().sum()) #결측치 확인

df.dropna(inplace=True)
print(df.isnull().sum()) #결측치 있는 행 삭제