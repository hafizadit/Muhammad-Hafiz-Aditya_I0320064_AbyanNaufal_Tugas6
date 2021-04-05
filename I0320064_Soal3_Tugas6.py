# Header
print("")
print("="*50)
end = "Soal 3 : Cek Bilangan Prima"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")

for x in range(1,30):
    if x == 1:
        print(x,"bukan prima")
    elif x == 2:
        print(x, "adalah bilangan prima")
    else:
        for i in range(2,x):
            if x % i == 0:
                print(x, "bukan prima")
                break
        else:
            print(x, "adalah bilangan prima")

# Footer
print("")
print("="*50)
end = "Selesai"
endCenter = end.center(50)
print(endCenter)
print("="*50)
print("")