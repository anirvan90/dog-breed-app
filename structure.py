import pandas as pd
import os

df = pd.read_csv('./labels.csv')

for row in df.iterrows():
    if not os.path.exists('./data/train/'+row[1]['breed']):
        os.makedirs('./data/train/'+row[1]['breed'])

    id = row[1]['id']
    breed ='./data/train/'+ row[1]['breed']
    os.system('mv ./data/train/' + id + '.jpg' + ' ./' + breed + '/')
