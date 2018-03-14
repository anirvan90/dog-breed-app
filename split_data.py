import os


def move_file(num_files, path, breed):
    os.chdir(path)
    dest = '../../valid/' + breed
    os.system(
        'ls | gshuf -n ' + str(num_files) + ' | xargs -I {} mv {} ' + dest)


def split(train_path, split_pct):
    for breed in os.listdir(train_path):
        if not os.path.exists('./data/new_set/valid/' + breed):
            os.mkdir('./data/new_set/valid/' + breed)

        train_dirs = os.listdir(train_path + breed)
        num_files = len(train_dirs) // split_pct
        current_dir = os.getcwd()
        path = train_path + breed
        move_file(num_files, path, breed)
        os.chdir(current_dir)


split('./data/new_set/train/', 10)
