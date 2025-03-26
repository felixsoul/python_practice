import pandas as pd

data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]]

df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])

df.index.name = "user_id"
# print(df)
# df1 = df.reset_index()
# print(df1)
# print(df1.index)
# print(df1.info())

# df2 = df1.set_index("name")
# print(df2)
# df3 = df.reindex([999, 1000, 1001, 1004])
# print(df3)
# print(df.sort_index())
# print(df.sort_values(["continent", "age"]))
# print(df.columns)
# df.columns.name = "properties"
# print(df)
# print(df.info())
# print(df)
# print(df.columns)
# print(df.loc[1000, "country"])
# print(df.loc[:, "country"])
# print(df.loc[:, ["country"]])
# print(df.loc[:, ["country", "age"]])
# print(df.loc[:, "name":"country"])
# print(df.loc[1000, :])
# print(df.loc[[1000], :])
# print(df.loc[[1000, 1003], :])
# print(df.loc[1001:1002, :])
# print(df.loc[[1001, 1002], "age"])
# print(df.loc[1000, ["country", "age"]])
# print(df.loc[:1002, ["name", "country"]])
# print(df["country"])
# print(df[["country", "name"]])
# print(df)
# print(df.iloc[1, 3])
# print(df.iloc[:, 2])
print(df.iloc[:, [2]])
print(df.iloc[:, [2, 1]])
print(df.iloc[:, [2, 0]])

tf = (df["age"] > 40) & (df["country"] == "USA")
print(tf)
print("hello gitee")
