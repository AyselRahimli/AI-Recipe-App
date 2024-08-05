import streamlit as st
import requests

st.title('Ingredient-Based Recipe, Nutrition, and Waste Reduction App')

ingredients = st.text_input('Enter your ingredients (comma-separated)')
if ingredients:
    st.write(f'You entered: {ingredients}')
    
    # Fetch recipes
    def fetch_recipes(ingredients):
        app_id = '98f629fc'
        app_key = '
26eb59d642eee5f98cd5a20e0d121acc	—
'
        url = f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}"
        response = requests.get(url)
        data = response.json()
        return data['hits']
    
    recipes = fetch_recipes(ingredients)
    st.subheader('Recipes:')
    for recipe in recipes:
        st.write(recipe['recipe']['label'])
        st.write(f"Calories: {recipe['recipe']['calories']}")
        st.write(f"URL: {recipe['recipe']['url']}")
        st.image(recipe['recipe']['image'])
