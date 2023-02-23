dadu_1 = int(input('Masukan dadu 1 : '))
dadu_2 = int(input('Masukan dadu 2 : '))
dadu_3 = int(input('Masukan dadu 3 : '))
dadu = [1,2,3,4,6]
jumlah = dadu_1+dadu_2+dadu_3    
if jumlah == 18 :
        print('Royal ')
elif dadu_1 == dadu_2 == dadu_3:
        print('Triple')
elif dadu_1 == dadu_2 and dadu_1 != dadu_3:
        print('Double')
elif dadu_2== dadu_3 and dadu_3 != dadu_1:
        print('double')
elif dadu_3 == dadu_1 and dadu_3 != dadu_2:
        print('double')
elif (dadu_1==4 or dadu_1==5 or dadu_1==6)and(dadu_2==4 or dadu_2==5 or dadu_2==6)and (dadu_3==4 or dadu_3==5 or dadu_3==6):
        print('flush')
else:
        print('single')

