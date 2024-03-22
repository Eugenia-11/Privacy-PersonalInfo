import pandas as pd

# 파일 경로 설정
file_path = 'ex1.csv'

# CSV 파일을 읽어 DataFrame 객체를 생성
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='euc-kr')

# '나이' 컬럼의 모든 값의 합계를 계산
age_total = sum(df['나이'])
# '나이' 컬럼의 데이터 개수를 계산
age_count = len(df['나이'])
# 평균을 수동으로 계산
age_mean = age_total / age_count

# '나이' 컬럼의 모든 값을 평균 나이로 대체
df['나이'] = age_mean

# 변경된 전체 데이터프레임 출력
print(df)