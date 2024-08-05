import streamlit as st
import requests

st.title('Recipe AI applications for Pantry')

ingredients = st.text_input('Enter your ingredients (comma-separated)')
if ingredients:
    st.write(f'You entered: {ingredients}')
    
    # Fetch recipes
    def fetch_recipes(ingredients):
        app_id = '98f629fc'  # Replace with your actual App ID
        app_key = '26eb59d642eee5f98cd5a20e0d121acc'  # Replace with your actual App Key
        url = f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}"
        response = requests.get(url)
        data = response.json()
        return data['hits']
    
    recipes = fetch_recipes(ingredients)
    st.subheader('Recipes:')
    for recipe in recipes:
        st.write(recipe['recipe']['label'])
        st.write(f"Calories: {recipe['recipe']['calories']:.2f}")
        st.write(f"URL: {recipe['recipe']['url']}")
        st.image(recipe['recipe']['image'])
