import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Virat_Kohli.csv")
# print(df.head())


# print("Total Runs:", df["Runs"].sum())

# print("Balls faced:",df["BF"].sum())

# print("Avg strike rate:", df["SR"].mean())

# print(df["Pos"].head(20))

positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})

# print(df[["Runs", "Pos"]])

# pos_count = df["Pos"].value_counts()

# print(pos_count)
# print(type(pos_count))

# pos_counts_values = pos_count.values
# pos_counts_lables = pos_count.index

# fig=plt.figure(figsize=(10, 7))
# plt.pie(pos_counts_values, labels=pos_counts_lables)
# plt.show()


def show_pie_plots(df, key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_lables= counts.lables
    
    fig = plt.figure(figsize=(10, 7))
    plt.pie(count_values, count_labels=count_lables)
    plt.show()
show_pie_plots(df, "Opposition")
    