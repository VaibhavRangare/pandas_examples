import pandas as pd

file_path = 'C:\\Resources\\Program_Xl_Sheets\\Satisfaction_Survey.csv'
# file_path = 'entities.csv'
df = pd.read_csv(file_path)
values = df.head()                           # read the first 5 lines including the header
print(values)                                # print the data frame

# age_range = df[['Age Range']]                  # column names are case sensitive
age_range = df['Age Range']
print(age_range)

multiple_values = df[['Age Range', 'Class', 'Gender']]
print(multiple_values)
print("Individual Value")
print(multiple_values.iloc[0, 0])
print(df.loc[0, 'Age Range'])
z = values.iloc[0:3, 0:3]
print(z)
age = df['Satisfaction'].unique()
print(age)

df1 = df[df['Age'] > 52]
print(df1.head())
df1.to_csv('C:\\Resources\\Program_Xl_Sheets\\Satisfaction_Survey1.csv')
