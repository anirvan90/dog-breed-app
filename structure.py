import pandas as pd
import os

df = pd.read_csv('./labels.csv')

for row in df.iterrows():
    if not os.path.exists(row[1]['breed']):
        os.makedirs(row[1]['breed'])

    id = row[1]['id']
    breed = row[1]['breed']
    os.system('mv ./train/' + id + '.jpg' + ' ./' + breed + '/')
