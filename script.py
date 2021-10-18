#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading data into a dataframe
df = pd.read_csv('clean_titanic_data.csv')

#dealing with user input
def input_():
    #prompting the user to pick a way to view data.
    user_input = input('type "C" for conclusion, "H" for data header, "G" for general statics, or type a specific column name to do analysis')
    #checking if the user entered a valid input.
    if user_input.lower() not in 'chg' or user_input.lower() not in df.columns:
        print('not valid input, please try again.')
        #recursive call for the function.
        input_()
    #dealing with various user inputs.   
    #printing conclusion.
    elif user_input.lower() == 'c':
        print('after the analysis, we found that women had a much higher rate of survival than men, age showed a negative corrletion with survival, the fare and ticket class of passengers both showed great effect on survival, the higher the class and the fare, the higher chance of survival, having relations up to a certain number is fine, but above a certain threshold it can be deadly.')
    #printing data header.
    elif user_input.lower() == 'h':
        print(df.head())
    #printing general statics and information.
    elif user_input.lower() == 'g':
        print(df.describe()) , print(df.info())

        


