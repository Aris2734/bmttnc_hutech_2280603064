n = input("Nhap cac so: ").split(',')
result = [i for i in n if int(i) % 5 == 0]
print(",".join(result))
