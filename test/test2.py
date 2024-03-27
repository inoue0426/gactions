import pandas as pd
import numpy as np

def split_date():

    # Read data
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    # Drop empty rows
    data = data.dropna(how="all")

    return data


def split_date():
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    data = data.dropna(how="all")
    
    
    data = data.dropna(axis=1)




    # Split the first column
    data = data["Päivämäärä"].str.split(expand=True)

    # Finnish to English
    data.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    # Finnish to English
    data["Weekday"] = data["Weekday"].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})

    # Finnish to English
    data["Month"] = data["Month"].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12})

    # Convert to integers
    data["Day"] = data["Day"].map(int)
    data["Year"] = data["Year"].map(int)
    
    # Convert to integers
    data["Hour"] = data["Hour"].str.split(":", expand=True)[0].map(int) 

    return data