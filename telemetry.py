import csv
import pandas.io.api
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


fieldnames = ["Club", "Value", "User"]

clubs = [None, None, None]


def create():
    with open("data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()


def append(data):
    user = "user" + str(pd.read_csv('data.csv').groupby('User').size().size)
    pd.DataFrame({
        "Data": ["ADC", "ASU", "BSU"],
        "Value": [data[0], data[1], data[2]],
        "User": [user, user, user]
        }).to_csv('data.csv', mode='a', index=False, header=False)


def chart():
    df = pd.read_csv("data.csv")
    sb.catplot(data=df, x = df['Club'], y = df['Value'], hue = df['User'], kind="swarm")
    plt.show()
