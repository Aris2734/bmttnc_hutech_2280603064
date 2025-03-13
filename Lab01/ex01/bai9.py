def IsPrime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False 
    return True  

def main():
    n = int(input("Nhap so: "))  
    if IsPrime(n):
        print("La so nguyen to")  
    else:
        print("Khong phai so nguyen to")  


main()
