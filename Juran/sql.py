import pandas as pd
from sqlalchemy import create_engine

# MySQL 데이터베이스 연결 정보 설정
db_user = 'fisaai'
db_password = 'woorifisa3!W'
db_host = '118.67.131.22'
db_port = '3306'
db_name = 'juran'

# SQLAlchemy 엔진 생성
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# CSV 파일 경로
csv_file_path = 'menu.csv'

# CSV 파일 읽기
df = pd.read_csv(csv_file_path)
print(df.columns)
# CSV 데이터 삽입 전 열 이름을 테이블의 열 이름과 일치시키기
df.columns = [
    'food_name', 'energy_kcal', 'moisture_g', 'protein_g', 'fat_g', 'carbohydrate_g', 'sugar_g',
    'sodium_mg', 'potassium_mg', 'calcium_mg', 'iron_mg', 'vitamin_a_ug_rae', 'vitamin_c_mg',
    'vitamin_d_ug', 'saturated_fat_g', 'cholesterol_mg'
]

# 데이터베이스에 데이터 삽입
try:
    # if_exists='append' 옵션을 사용하여 테이블에 데이터 추가
    df.to_sql('nutrition_info', con=engine, if_exists='append', index=False)
    print("Data inserted successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
