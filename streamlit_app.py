import streamlit
import pandas

# streamlit.title('My Parents New Healthy Diner')

# streamlit.header('Breakfast Favorites')
# streamlit.text(' 🥣 Omega 3 & blueberry Oatmeal')
# streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
# streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
# streamlit.text(' 🥑🍞 Avacado Toast ')

# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_excel('C:\Users\anusha.s31\Documents\Learnings\Snowflake\Fruits_streamlit.xlsx',index_col=0)
streamlit.dataframe(my_fruit_list)

