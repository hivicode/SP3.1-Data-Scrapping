import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

def read_data(path, limit):
    with open(path,'rt') as file:
        count = 0
        for line in file:
            if count == limit*2:
                break
            print(line.replace("\n",""))
            count += 1

def does_file_exist(path):
    return os.path.isfile(path)

def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
    else:
        print("file tidak ada")