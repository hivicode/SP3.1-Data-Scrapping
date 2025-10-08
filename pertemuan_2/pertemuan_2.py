def ucapan(text):
    print(text)

ucapan("hello world!")

#membuat directory/folder
import os

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

create_directory("scrapping")


#membuat file kosong
def create_new_file(path):
    f=open(path,'w')
    f.write("")
    f.close()

create_new_file("scrapping/test.txt")


#menulis isi ke dalam file yang sudah ada
def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

write_to_file("scrapping/test.txt", "ini adalah data yang akan digunakan untuk menampung big data \n")


#menghapus isi file
def clear_file(path):
    f=open(path,'w')
    f.close()

clear_file("scrapping/test.txt")


#validasi ekstensi file
import os

def does_file_exist(path):
    return os.path.isfile(path)

print(does_file_exist("scrapping/test.txt"))


#membaca file
def read_data(path):
    with open(path,'r') as file:
        for line in file:
            print(line)

read_data("scrapping/test.txt")
read_data("data_scrapping/2_pertemuan2.py")


#menghapus file
def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
    else:
        print("file tidak ada")

remove_file('scrapping/test.txt')