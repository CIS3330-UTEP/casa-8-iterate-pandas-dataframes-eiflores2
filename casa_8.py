import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

print("Given Dataframe :\n", df)
print("\nIterating over rows using Iterrows() method: \n")

# show the first 10 rows
limit = 10
# name Index and rows using Iterrows method
for index,row in df.iterrows():
    if index >= limit:
        break
    # print the position of the index
    print(f'row{index} data: ')
    # print the rows of each column
    print(f"Name: {row['name']}, Currency Code: {row['currency_code']}")
