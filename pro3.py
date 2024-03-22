import pandas as pd
import random

# 파일 경로 설정
file_path = 'ex1.csv'

# CSV 파일을 읽어 DataFrame 객체를 생성
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='euc-kr')

# 데이터의 전체 길이와 표본의 크기
n = 5  # 추출할 표본의 개수
data_length = len(df)  # 데이터셋의 전체 길이

# 계통적 표본 추출을 위한 샘플 간격 (k) 결정
k = data_length // n

# 시작점 무작위 선택
start = random.randint(0, k - 1)

# 계통적 표본 추출
selected_indices = [i for i in range(start, data_length, k)[:n]]

# 추출된 인덱스에 해당하는 행을 가져옴
systematic_sampled_df = df.iloc[selected_indices]

# 추출된 샘플을 출력
print(systematic_sampled_df)