import os

train_src = './data/new_set/train/'
train_dst = './data/train/'

valid_src = './data/new_set/valid/'
valid_dst = './data/valid/'


def move(src, dst):
    breeds = os.listdir(src)
    for breed in breeds:
        os.system('mv ' + src + breed + '/* ' + dst + breed)


move(train_src, train_dst)
move(valid_src, valid_dst)