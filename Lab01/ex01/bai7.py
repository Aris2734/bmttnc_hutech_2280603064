s = list(input("Nhap chuoi: "))
b = []
for i in range(len(s)):
    b.append(s.pop())
print("".join(b)