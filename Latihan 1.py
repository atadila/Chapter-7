dir = input("Masukkan Direktori & Nama File : ")

try:
    file = open(dir, "r")
    print("Isi file", dir,"adalah :\n",file.read())

except FileNotFoundError:
    print("File Anda Tidak Ditemukan")