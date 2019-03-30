import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(1)

#take in the information for a person as a dataframe
df = pd.read_csv(r"Person1.csv")

#fill the NaN's with zeros
df.fillna(0, inplace=True)

#turn the dataframes into an array
df_transportation = df["Transportation"].tolist()
df_ent = df["Entertainment"].tolist()
df_groceries = df["Groceries"].tolist()

print(df_transportation)

def plotInfo(data, color='red'):
    y = [x for x in range(len(data))]

    print(y)
    plt.scatter(data, y, 1.5, color)


plotInfo(df_transportation, color='blue')

plt.show()