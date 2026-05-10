mas = [x+1 for x in range(16)]
fir = mas[0:4]
sec = mas[4:8]
thi = mas[8:12]
fou = mas[12:16]
res = [fir, sec, thi, fou]
for mat in res:
    print(*mat)