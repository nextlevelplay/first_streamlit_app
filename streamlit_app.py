import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('🎮 Edvins Game 🎮')
answers_list = ["Yes", "No"]
answer_field = streamlit.multiselect("Will you play the game? Make a choice (yes / no): ", list(answers_list))

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

fruit_choise = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered: ', fruit_choise)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choise)
# streamlit.text(fruityvice_response.json())

fruityvice_normal_view = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normal_view)


fruit_load_list = requests.get("https://fruityvice.com/api/fruit/all")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)





# from random import shuffle

# mylist =["x", "x", 1]
# play = input("will you play the game? Write (yes / no): ")
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist

# shuffle_list(mylist)
# def game():
    
#     if play == "yes":
#         print("[ x | x | x ]")
#         number = int(input("Chose and write number from 1 to 3, wich 'x' from this table have number '1': "))
#         if number < 1 or number > 3:
#             print("Please next time write correct numbers!")
#         elif number >= 1 and number <=3:
#             if mylist[number-1] == 1:
#                 print("you win!")
#                 print(mylist)
#             else:
#                 print("Wrong!!")
#                 print(mylist)
#     else:
#         print("okay, see you next time")
# game()
