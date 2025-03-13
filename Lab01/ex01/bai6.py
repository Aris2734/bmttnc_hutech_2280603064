rowNum = int(input("Nhập số hàng: "))  
colNum = int(input("Nhập số cột: ")) 
a = []

for i in range(rowNum):
    row = [] 
    for j in range(colNum):
        value = int(input(f"Nhập giá trị cho phần tử tại hàng {i+1}, cột {j+1}: "))
        row.append(value)
    a.append(row)  

print("Ma trận đã nhập:")
for row in a:
    print(row)
