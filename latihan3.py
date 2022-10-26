# Input nilai variable
a = input("Masukan nilai a: ")
b = input("Masukan nilai b: ")

# Cetak nilai variable
print("Variable a = ", a)
print("Variable b = ", b)

# Cetak hasil operasi kedua variable dengan String Format
print("Hasil penggabungan {0} & {1} = %s" . format(a, b) % (a + b))

# Konversi nilai variable
a = int(a)
b = int(b)
print("Hasil penjumlahan {0} + {1} = %d".format(a, b) % (a + b))
print("Hasil pembagian {0} / {1} = %d".format(a, b) % (a / b))
