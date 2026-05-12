import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 




# 데이터 로드
df = pd.read_csv("산불발생이력.csv")

print("=== 기본 정보 ===")
print(df.shape)
print(df.dtypes)
print("\n=== 결측치 확인 ===")
print(df.isnull().sum())
print("\n=== 기본 통계 ===")
print(df.describe())