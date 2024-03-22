import pandas as pd
import random

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

# '우편번호' 컬럼에 랜덤 라운딩 처리를 적용합니다.
for i in range(len(df)):
    original_postal_code = int(df.at[i, '우편번호'])
    # 원본 우편번호에 -7에서 +7 사이의 값을 더함
    random_adjustment = random.randint(-7, 7)
    new_postal_code = original_postal_code + random_adjustment
    
    
    df.at[i, '우편번호'] = new_postal_code

# 변경된 전체 데이터프레임을 출력합니다.
print(df)
