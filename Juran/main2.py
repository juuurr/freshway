from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

# FastAPI app initialization
app2 = FastAPI()

# CORS middleware setup to allow requests from the frontend
app2.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Frontend URL (localhost:8080)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load the menu data
menu_data = pd.read_csv('menu.csv')

# Handle NaN and infinite values in the menu data
menu_data['나트륨(mg)'] = pd.to_numeric(menu_data['나트륨(mg)'], errors='coerce')  # Convert to numeric
menu_data.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace inf values with NaN
menu_data.fillna(0, inplace=True)  # Replace NaN with 0

# Recommendation functions
def recommend_for_diabetes(menu):
    filtered_menu = menu[(menu['당류(g)'] <= 3.3) & 
                         (menu['탄수화물(g)'] <= 13) &
                         (menu['나트륨(mg)'] <= 40)]
    return filtered_menu.sort_values(by=['당류(g)', '탄수화물(g)', '나트륨(mg)'])

def recommend_for_hypertension(menu):
    filtered_menu = menu[(menu['포화지방산(g)'] <= 1.4) & 
                          (menu['콜레스테롤(mg)'] <= 14) &
                          (menu['지방(g)'] <= 5) &
                          (menu['나트륨(mg)'] <= 40)]
    return filtered_menu.sort_values(by=['포화지방산(g)', '콜레스테롤(mg)', '지방(g)', '나트륨(mg)'])

def recommend_for_cad(menu):
    filtered_menu = menu[(menu['콜레스테롤(mg)'] <= 14) & 
                          (menu['포화지방산(g)'] <= 1.4) & 
                          (menu['나트륨(mg)'] <= 40)]
    return filtered_menu.sort_values(by=['콜레스테롤(mg)', '포화지방산(g)', '나트륨(mg)'])

def select_menu(menu_df):
    rice_menu = menu_df[menu_df['식품명'].str.contains('밥')]
    soup_menu = menu_df[menu_df['식품명'].str.contains('국')]

    # Check if rice_menu and soup_menu are not empty
    if not rice_menu.empty:
        rice_menu = rice_menu.sample(n=1)
    else:
        rice_menu = pd.DataFrame()  # Handle the case where there are no rice items
    
    if not soup_menu.empty:
        soup_menu = soup_menu.sample(n=1)
    else:
        soup_menu = pd.DataFrame()
    
    remaining_menu = menu_df[~menu_df['식품명'].str.contains('밥|국')]
    
    # Select 3 more random items from the remaining menu
    random_menu = remaining_menu.sample(n=3)
    
    # Combine the rice, soup, and random items
    final_menu = pd.concat([rice_menu, soup_menu, random_menu])
    
    # Shuffle the final menu to ensure randomness
    final_menu = final_menu.sample(frac=1).reset_index(drop=True)

    sum_columns = final_menu.drop('식품명', axis=1).sum()
    final_menu.loc[5] = sum_columns
    final_menu.at[5, '식품명'] = '합계'
    final_menu = final_menu.round(2)
    
    return final_menu.to_dict(orient="records")

# Define the API endpoint to get recommendations
@app2.get("/recommendations/all2")
def get_all_recommendations():
    # Get recommendations for different conditions
    diabetes_recommendations = select_menu(recommend_for_diabetes(menu_data))
    hypertension_recommendations = select_menu(recommend_for_hypertension(menu_data))
    cad_recommendations = select_menu(recommend_for_cad(menu_data))

    # Return recommendations as a dictionary
    all_recommendations = {
        '당뇨병': diabetes_recommendations,
        '고혈압': hypertension_recommendations,
        '동맥질환': cad_recommendations
    }
    
    return all_recommendations

# Run the FastAPI app (uncomment for execution outside Jupyter or in a script)
# uvicorn.run(app2, host="0.0.0.0", port=8001)