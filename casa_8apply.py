import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

s = df['local_price'].squeeze()

# check the prices of local price

def fun(currency):
    currency = float (currency)
    if currency < 3:
        return "Low"
    elif 3<= currency < 6:
        return "Normal"
    else:
        return "High"
    
new = s.apply(fun)

# Print first 5 elements
print(new.head(5))

# print last 5 elements
print(new.tail(5))