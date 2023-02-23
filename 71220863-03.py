p1 = int(input('Masukan Pemain 1 : '))
p2 = int(input('Masukan Pemain 2 : '))
p3 = int(input('Masukan Pemain 3 : '))

if p1 > 21:
    p1 = 0 
if p2 > 21:
    p2 = 0
if p3 > 21:
    p3=0


if p1 ==0 and p2 ==0 and p3 == 0 :
    print('tidak ada pemenang')
elif p1 == p2 == p3 :
    print('tidak ada pemenang')
else:
    if p1 == 21:
        print('pemenangnya adalah p1')
    elif p2 == 21:
        print('pemenangnya adalah p2')
    elif p3 == 21:
        print('pemenangnya adalah p3')
    else:
        diff_p1 = abs(21-p1)
        diff_p2 = abs(21-p2)
        diff_p3 = abs(21-p3)

        if p1 != 0 or p2!=0 or p3 !=0:
            min_diff = min(diff_p1,diff_p2,diff_p3)

            if min_diff == diff_p1 and min_diff==diff_p2:
                print('tidak ada pemenang ')
            elif min_diff == diff_p2 and min_diff==diff_p3:
                print('Tidak ada pemenang')
            elif min_diff== diff_p3 and min_diff==diff_p1:
                print('tidak ada pemenang ')
            else:
                if min_diff== diff_p1:
                    print('Pemenangnya adalah p1')
                elif min_diff== diff_p2:
                    print('pemenangnya adalah p2')
                else:
                    print('pemenangnya adalah p3')
        else:
            print('tidak ada pemenags')