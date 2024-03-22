import pandas as pd

# 파일 경로 설정
file_path = 'ex1.csv'

# CSV 파일을 읽어 DataFrame 객체를 생성
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='euc-kr')

# '나이' 컬럼을 10의 배수로 일반 라운딩 처리합니다.
for i in range(len(df)):
    df.at[i, '나이'] = round(df.at[i, '나이'] / 10) * 10

# 변경된 전체 데이터프레임을 출력합니다.
print(df)
