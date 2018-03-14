import os
import re

directory_list = os.listdir('./data/Images')
path = './data/Images/'
dest = './data/new_set/train/'
temp = []
for breed in directory_list:
    st = breed.split('-', 1)[1].lower()
    os.rename(path + breed, path + st)

os.system('mv '+path+'* '+dest)
