gio=float(input("Nhap so gio"))
luong=int(input("Nhap so luong"))
if gio > 44:
    sum=float((gio-44)*luong*1.5+44*luong)
else:
    sum=float(gio*luong)
    print("so tien thuc te nhan duoc",sum)