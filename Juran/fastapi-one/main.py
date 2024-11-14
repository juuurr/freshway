from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import uvicorn

# FastAPI app initialization
app = FastAPI()

# CORS middleware setup to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Frontend URL (localhost:8080)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# 메뉴 데이터 로드
file_path = 'menu.csv'
menu_df = pd.read_csv(file_path, encoding='utf-8').fillna(0)

# 건강 상태별 영양 기준과 가중치
health_conditions = {
    '저염식': {'나트륨(mg)': {'limit': 100, 'weight': 0.5}, '에너지(kcal)': {'limit': 500, 'weight': 0.3}, '지방(g)': {'limit': 20, 'weight': 0.2}},
    '저에너지식': {'에너지(kcal)': {'limit': 300, 'weight': 0.5}, '지방(g)': {'limit': 10, 'weight': 0.3}, '탄수화물(g)': {'limit': 50, 'weight': 0.2}},
    '당뇨식': {'당류(g)': {'limit': 10, 'weight': 0.4}, '탄수화물(g)': {'limit': 30, 'weight': 0.4}, '지방(g)': {'limit': 10, 'weight': 0.2}},
    '고단백식': {'단백질(g)': {'limit': 20, 'weight': 0.5}, '에너지(kcal)': {'limit': 600, 'weight': 0.3}, '지방(g)': {'limit': 15, 'weight': 0.2}}
}

# 점수를 1에서 5점 사이로 계산하는 함수 (가중치 적용)
def calculate_weighted_score(value, limit, weight):
    if value <= limit:
        return 5 * weight
    elif value <= limit * 1.2:
        return 4 * weight
    elif value <= limit * 1.5:
        return 3 * weight
    elif value <= limit * 2:
        return 2 * weight
    else:
        return 1 * weight

# 건강 상태에 따른 메뉴 추천 함수 정의
def recommend_menu_by_health_condition(condition, num_recommendations=5):
    condition_criteria = health_conditions[condition]
    menu_df['적합성 점수'] = 0

    # 각 영양소에 대해 점수를 계산하고 가중치를 적용하여 최종 점수 합산
    for nutrient, params in condition_criteria.items():
        limit = params['limit']
        weight = params['weight']
        menu_df['적합성 점수'] += menu_df[nutrient].apply(lambda x: calculate_weighted_score(x, limit, weight))

    # 밥과 국을 우선적으로 선택
    rice_menu = menu_df[menu_df['식품명'].str.contains('밥')].sample(n=1)
    soup_menu = menu_df[menu_df['식품명'].str.contains('국')].sample(n=1)
    
    # 나머지 메뉴에서 조건에 맞는 상위 메뉴를 무작위로 선택
    remaining_menus = menu_df[~menu_df['식품명'].str.contains('밥|국')].sort_values(by='적합성 점수', ascending=False)
    remaining_sampled = remaining_menus.sample(n=num_recommendations - 2, random_state=None)    

    # 밥, 국, 나머지 메뉴 합쳐서 최종 추천 리스트 작성
    recommended_menus = pd.concat([rice_menu, soup_menu, remaining_sampled]).head(num_recommendations)
    
    return recommended_menus[['식품명', '적합성 점수', '나트륨(mg)', '에너지(kcal)', '지방(g)', '당류(g)', '탄수화물(g)', '단백질(g)']].to_dict(orient='records')

# 모든 건강 상태에 대한 추천을 가져오는 엔드포인트
@app.get("/recommendations/all")
async def get_all_recommendations():
    all_recommendations = {}
    for condition in health_conditions:
        all_recommendations[condition] = recommend_menu_by_health_condition(condition)
    return all_recommendations

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)