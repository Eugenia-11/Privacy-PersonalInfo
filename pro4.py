import pandas as pd
import random

# 파일 경로 설정
file_path = 'ex1.csv'

# CSV 파일을 읽어 DataFrame 객체를 생성
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='euc-kr')

# '교육 수준' 별로 데이터 프레임을 분할
strata = df.groupby('교육 수준')

# 총 추출할 표본의 수
n = 5
# 각 층에서 추출할 표본의 수 계산
strata_sample_sizes = {stratum: n // len(strata) for stratum in strata.groups.keys()}
# 남은 표본 할당
remaining_samples = n - sum(strata_sample_sizes.values())
for stratum in random.sample(list(strata.groups.keys()), remaining_samples):
    strata_sample_sizes[stratum] += 1

# 각 층에서 표본 추출
stratified_samples_list = []
for stratum, sample_size in strata_sample_sizes.items():
    stratified_samples_list.append(strata.get_group(stratum).sample(n=sample_size))

# 모든 표본을 하나의 DataFrame으로 결합
stratified_samples = pd.concat(stratified_samples_list)

# 추출된 샘플을 출력
print(stratified_samples)