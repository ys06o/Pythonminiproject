# # [핵심 1] 좌표계 변환 및 한글 칼럼화
# # TM중부(5179) 좌표를 위경도(4326)로 변환하여 범용성 확보
# transformer = Transformer.from_crs("EPSG:5179", "EPSG:4326", always_xy=True)
# final_df[['위도', '경도']] = final_df.apply(
#     lambda r: pd.Series(transformer.transform(r['RBP_X'], r['RBP_Y'])[::-1]), axis=1
# )

# # [핵심 2] 역지오코딩을 통한 파생 변수(읍면동) 생성
# # 산불 데이터와의 결합을 위해 좌표를 행정구역 텍스트로 변환
# def get_detailed_addr(lat, lon):
#     location = reverse((lat, lon), language='ko')
#     if location:
#         addr = location.raw.get('address', {})
#         # 읍/면/동 정보를 우선적으로 추출하여 결합 키 생성
#         town = addr.get('town', addr.get('village', addr.get('suburb', '')))
#         return pd.Series([location.address, town])

# # [핵심 3] 데이터 최적화 및 상수 컬럼 삭제
# # 분석에 필요한 핵심 컬럼만 선택하고 변별력 없는 데이터 자동 제거
# columns_to_keep = ['지역', '시설거리(km)', '개설연도', '위도', '경도', '상세주소', '읍면동']
# final_df = final_df[columns_to_keep]
# # 값이 1종류뿐인 불필요한 컬럼 자동 삭제
# final_df = final_df.drop(final_df.nunique()[final_df.nunique() <= 1].index, axis=1)