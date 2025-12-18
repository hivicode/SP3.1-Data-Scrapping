# Pertemuan 2 - File Operations

Pertemuan ini membahas operasi-operasi dasar file dan directory dalam Python.

## Metode yang Dipelajari

### 1. Ucapan (Print Function)
**Fungsi**: Menampilkan teks ke console
```python
def ucapan(text):
    print(text)
```

**Contoh Output**:
```
hello world!
```

### 2. Membuat Directory/Folder
**Fungsi**: Membuat folder baru jika belum ada
```python
def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
```

**Contoh Output**:
```
# Folder 'scrapping' akan dibuat di direktori saat ini
# Tidak ada output di console, folder dibuat secara silent
```

### 3. Membuat File Kosong
**Fungsi**: Membuat file baru dengan isi kosong
```python
def create_new_file(path):
    f=open(path,'w')
    f.write("")
    f.close()
```

**Contoh Output**:
```
# File 'scrapping/test.txt' akan dibuat
# Tidak ada output di console, file dibuat secara silent
```

### 4. Menulis ke File
**Fungsi**: Menambahkan data ke file yang sudah ada
```python
def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')
```

**Contoh Output**:
```
# Data akan ditambahkan ke file scrapping/test.txt
# Tidak ada output di console, data ditulis secara silent
```

### 5. Menghapus Isi File
**Fungsi**: Mengosongkan isi file
```python
def clear_file(path):
    f=open(path,'w')
    f.close()
```

**Contoh Output**:
```
# File akan dikosongkan
# Tidak ada output di console, file dikosongkan secara silent
```

### 6. Validasi Ekstensi File
**Fungsi**: Mengecek apakah file ada atau tidak
```python
def does_file_exist(path):
    return os.path.isfile(path)
```

**Contoh Output**:
```
True
```

### 7. Membaca File
**Fungsi**: Membaca dan menampilkan isi file
```python
def read_data(path):
    with open(path,'r') as file:
        for line in file:
            print(line)
```

**Contoh Output**:
```
# Jika file ada dan berisi data:
ini adalah data yang akan digunakan untuk menampung big data 

# Jika file kosong atau tidak ada:
# Tidak ada output atau error message
```

### 8. Menghapus File
**Fungsi**: Menghapus file jika ada
```python
def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
    else:
        print("file tidak ada")
```

**Contoh Output**:
```
# Jika file ada:
# File akan dihapus tanpa output

# Jika file tidak ada:
file tidak ada
```

## Cara Menjalankan

1. Pastikan Python sudah terinstall
2. Jalankan file `pertemuan_2.py`
3. Perhatikan output di console dan perubahan file/directory

## Struktur File yang Dibuat

```
scrapping/
└── test.txt (akan dibuat, ditulis, dibaca, dan dihapus)
```
