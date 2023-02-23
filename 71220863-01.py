masukanNilai = int(input('Masukan Nilai Anda : '))
masukanBatas = int(input('masukan Batas Nilai : '))
masukanJarak = int(input('masukan jarak Nilai : '))

if masukanNilai >= masukanBatas:
    print('A')
elif masukanNilai >=(masukanBatas-masukanJarak):
    print('A-')
elif masukanNilai>= (masukanBatas-masukanJarak*2):
    print('B+')
elif masukanNilai>=(masukanBatas-masukanJarak*3):
    print('B')
elif masukanNilai>=(masukanBatas-masukanJarak*4):
    print('B-')
elif masukanNilai>=(masukanBatas-masukanJarak*5):
    print('C+')
elif masukanNilai>=(masukanBatas-masukanJarak*6):
    print('C')
elif masukanNilai>=(masukanBatas-masukanJarak*7):
    print('D')
else:
    print('E')