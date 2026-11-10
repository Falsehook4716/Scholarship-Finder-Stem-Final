import csv
import pandas.io.api
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


c_fieldnames = ["Club", "Value", "User"]

clubs = [None, None, None]
q_data = [None, None, None, None, None, None]

q_fieldnames = ["Gov_Aid", "GPA", "Minority", "Extracurricular", "Volunteer", "Income"]

def create():
    with open("c_data.csv", "w") as f:
        writer = csv.DictWriter(f, c_fieldnames)
        writer.writeheader()

    with open("q_data.csv", "w") as f:
        writer = csv.DictWriter(f, q_fieldnames)
        writer.writeheader()

def q_append(data):
    user = "user" + str(pd.read_csv('q_data.csv').groupby('User').size().size)
    pd.DataFrame({
        "Club": ["Gov_Aid", "GPA", "Minority", "Extracurricular", "Volunteer", "Income"],
        "Value": [data[0], data[1], data[2], data[3], data[4], data[5]],
        "User": [user, user, user, user, user, user]
        }).to_csv('data.csv', mode='a', index=False, header=False)

def c_append(data):
    user = "user" + str(pd.read_csv('c_data.csv').groupby('User').size().size)
    pd.DataFrame({
        "Data": ["ADC", "ASU", "BSU"],
        "Value": [data[0], data[1], data[2]],
        "User": [user, user, user]
        }).to_csv('data.csv', mode='a', index=False, header=False)


def c_chart():
    df = pd.read_csv("c_data.csv")
    sb.catplot(data=df, x = df['Club'], y = df['Value'], hue = df['User'], kind="swarm")
    plt.show()
def q_chart():
    df = pd.read_csv("q_data.csv")
    sb.catplot(data=df, x = df['Data'], y = df['Value'], hue = df['User'], kind="swarm")
    plt.show()
