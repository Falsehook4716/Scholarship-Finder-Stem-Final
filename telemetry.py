import csv
import pandas.io.api
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


fieldnames = ["User", "Data1", "Data2", "Data3"]

def create():
    with open("data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()


def append(data1=None, data2=None, data3=None):
    pd.DataFrame({
        "User": ["user" + str(pd.read_csv('data.csv').groupby('User').size().size)],
        "Data1": [data1],
        "Data2": [data2],
        "Data3": [data3],
        }).to_csv('data.csv', mode='a', index=False, header=False)


def chart():
    sb.catplot(data=pd.read_csv("data.csv"), x="User", y="Data1", kind="bar")
    plt.show()

