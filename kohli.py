import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Virat_Kohli.csv")

# print(df)

# print(df.head(10))

# df.info()
# print(df.shape)

# print(df["Opposition"].describe())

# run_frequency = df["Opposition"].value_counts()
# print(run_frequency)

# vs_ausis = df[df["Opposition"]=="v Australia"]
# print(vs_ausis)

# centuryy=df[df["Runs"]>= 100]
# print(centuryy)
# print("\n")
# sr=df[df["SR"]>100]
# print(sr)
# print("\n")
# sri_century= df[(df["Opposition"]=="v Sri Lanka") & (df["Runs"]>=100)]
# print(sri_century)


def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"]= df["Runs"].apply(find_centuries)

print(df.tail(10))