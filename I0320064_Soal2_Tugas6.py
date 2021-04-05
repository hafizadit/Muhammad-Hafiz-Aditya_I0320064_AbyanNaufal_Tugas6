# Header
print("")
print("="*50)
end = "Soal 2"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")

n = int(input("Masukkan jumlah data yang akan dimasukkan :"))
print("")

data = []

i = 1
while i <= n:
    nilai = int(input("Masukkan nilai ke-{} :".format(i)))
    data.append(nilai)
    i += 1

rerata = sum(data)/n
print("\nNilai rata-rata data anda adalah : {}".format(rerata))

# Footer
print("")
print("="*50)
end = "Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")