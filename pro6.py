import pandas as pd

# 파일 경로 설정
file_path = 'ex1.csv'

# CSV 파일을 읽어 DataFrame 객체를 생성
try:
    df = pd.read_csv(file_path, encoding='cp949')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='euc-kr')

# '아이디' 컬럼을 전체 마스킹 처리합니다.
df['아이디'] = 'MASKED'

# '우편번호' 컬럼을 부분 마스킹 처리합니다.
# 우편번호가 숫자형 데이터인 경우 문자열로 변환
# for 루프 사용
for i in range(len(df)):
    # 우편번호를 문자열로 변환
    postal_code_str = str(df.at[i, '우편번호'])
    # 부분 마스킹 처리
    df.at[i, '우편번호'] = postal_code_str[:2] + 'XXX' + postal_code_str[5:]

# 변경된 전체 데이터프레임을 출력합니다.
print(df)
