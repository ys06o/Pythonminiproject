import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 라이브러리)
import pandas as pd # 판다스(데이터 표 관리)
import koreanfont # 그래프 한글 꺠짐 방지
import json  # json 파일 load 용도
import seaborn as sns  # 



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


# -----------------------------------------------------------------

df_전지역 = pd.concat( [df_강원특별자치도 , df_경기도, df_경상남도, df_경상북도, df_광주광역시, 
                       df_대구광역시, df_대전광역시, df_부산광역시,  df_서울특별시, df_세종특별자치시, 
                       df_울산광역시 , df_인천광역시 , df_전라남도 , df_전북특별자치도 , df_충청남도 ,df_충청북도], ignore_index=True )

print(df_전지역)            