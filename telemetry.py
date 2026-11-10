import csv
import pandas.io.api
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import math


fieldnames = ["Data", "Value", "User"]

def create():
    with open("data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()


def append(data1=None, data2=None, data3=None):
    user = "user" + str(pd.read_csv('data.csv').groupby('User').size().size)
    pd.DataFrame({
        "Data": ["Data1", "Data2", "Data3"],
        "Value": [data1, data2, data3],
        "User": [user, user, user]
        }).to_csv('data.csv', mode='a', index=False, header=False)


def chart():
    df = pd.read_csv("data.csv")
    sb.catplot(data=df, x = df['Data'], y = df['Value'], hue = df['User'], kind="swarm")
    plt.show()
