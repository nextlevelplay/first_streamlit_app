import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put some choose availability to customers
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) # pre-selected fruits

fruit_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)

streamlit.header('Fruity Vice Advice')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
# streamlit.text(fruityvice_response.json())

fruityvice_normal_view = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normal_view)
