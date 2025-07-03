import pandas as pd
import os

data = {'name':['orbit','rdx','bamdi'],
        'age':[7,2,19],
        'city': ['delhi','haridwar','pauri ']}

df= pd.DataFrame(data)

new_row={'name':'do','age':10,'city':'taxes'}
df.loc[len(df.index)]=new_row

data_dir= 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")