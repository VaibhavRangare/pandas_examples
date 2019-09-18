import pandas as pd

dict1 = {
    "Movie Name": ["Matrix", "Zero", "Pink"],
    "Rating": [6.5, 7.5, 8.5]
}
df = pd.DataFrame(dict1)
values = df.head()
print(values)
