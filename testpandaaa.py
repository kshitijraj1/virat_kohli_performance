import pandas as pd

data= {
    "apples":[4,3,6,1],
    "orange":[3,7,4,1]
}

index_titles=[
    "Aaron", "Shaun", "James", "Wilson"
]
df = pd.DataFrame(data, index= index_titles)

# print(df)

print(df.loc["Aaron"])

print(df.loc["Aaron"]["apples"])

print(df.loc["Aaron"].iloc[1:])