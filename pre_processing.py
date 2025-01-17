import pandas as pd

# 데이터 로드
file_path = "07388.csv"  # 파일 경로
data = pd.read_csv(file_path)

# 데이터 구조 확인
print(data.info())
print(data.head())

# 시간(Time) 컬럼이 초 단위로 되어 있으므로 가독성을 위해 분 단위로 변환 (선택)
data['Time_minutes'] = data['Time'] / 60

# 결측값 확인
print(data.isnull().sum())
