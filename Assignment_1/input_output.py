import sys
import csv
import time
import colorama
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from colorama import init
from selenium import webdriver
from colorama import Fore, Back, Style

# Example of input
def input():
    # filename in refrence to where youtube dataset is stored
    filename = '/Users/fagirtmi1/Documents/UNCC/Coursework/Senior_Year/Fall_2018/ITCS_4102/Project/Assignment_1/Datasets/Youtube/data.csv'
    
    data = pd.read_csv(filename) # You the python data-structure 'dataframes' to load the csv
    
    return data # return the filename corresponding to the location of the youtube dataset

# Example of output
def output():
    data = input() # Get the Youtube dataset in the form of a pandas dataframe from the input method

    # Print the top 10 rows
    print(Fore.BLUE +  Style.BRIGHT + "\nTop 10 rows in Youtube dataset.\n")
    print(data.head(10))

    # Print general info about the youtube datset using the 'info' method from pandas
    print(Fore.BLUE +  Style.BRIGHT + "\nYoutube dataset high-level info.\n")
    print(data.info())
    
    # Get the description (mean, mode, etc..) from only the numeric columns from the youtube dataset
    print(Fore.BLUE +  Style.BRIGHT + "\nYoutube numerical columns description.\n")
    print(data.describe(include=[np.number]))

    # Check for any null values using the 'isna()' pandas method
    print(Fore.BLUE +  Style.BRIGHT + "\nCheck for any null values in the Youtube dataset.\n")
    print(data.isna().sum())

    return data # return the Youtube dataframe

if __name__ == '__main__':
    init(autoreset=True)
    colorama.init()
    
    print("Current date & time " + time.strftime("%c") + Fore.GREEN +  Style.BRIGHT + " Youtube Dataset Imported.")

    output() # Run the Script
