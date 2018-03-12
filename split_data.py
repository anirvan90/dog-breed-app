import os


def move_file(num_files, path, breed):
    os.chdir(path)
    dest = '../../valid/' + breed
    os.system(
        'ls | shuf -n ' + str(num_files) + ' | xargs -I {} mv {} ' + dest)


def split(train_path, split_pct):
    for breed in os.listdir(train_path):
        if not os.path.exists('./data/valid/' + breed):
            os.mkdir('./data/valid/' + breed)

        train_dirs = os.listdir('./data/train/' + breed)
        num_files = len(train_dirs) // split_pct
        current_dir = os.getcwd()
        path = './data/train/' + breed
        move_file(num_files, path, breed)
        os.chdir(current_dir)


split('./data/train', 3)
