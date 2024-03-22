import pandas as pd
import random

# 파일 경로 설정
file_path = 'ex1.csv'

# CSV 파일을 읽어 DataFrame 객체를 생성
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='euc-kr')

# 데이터의 전체 길이에서 n개의 무작위 인덱스를 추출하는 과정
n = 3  # 추출할 표본의 개수
data_length = len(df)  # 데이터셋의 전체 길이
selected_indices = []  # 선택된 인덱스를 저장할 리스트

while len(selected_indices) < n:
    # 무작위 인덱스를 생성합니다.
    index = random.randrange(data_length)
    # 중복된 인덱스가 아니라면 선택된 인덱스 리스트에 추가합니다.
    if index not in selected_indices:
        selected_indices.append(index)

# 추출된 인덱스에 해당하는 행을 가져옴
sampled_df = df.iloc[selected_indices]

# 추출된 샘플을 출력
print(sampled_df)