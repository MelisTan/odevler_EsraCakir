s1 = input("Birinci sayıyı giriniz: ")
s2 = input("İkinci sayıyı giriniz: ")
n = 0

while(n == 0):
    islem = input("Yapılmasını istediğiniz işleme göre (+,-,*,/) operatörlerinden birini giriniz,\n"+
                  "Programdan çıkmak için (!) giriniz...")
        
    if (s1.isdigit() == True) and (s2.isdigit() == True):     
        s1 = float(s1)
        s2 = float(s2)
        if islem == "+":
            print("Toplam: "+ str(s1+s2))
        elif islem == "-":
            print("Fark: "+ str(s1-s2))
        elif islem == "*":
            print("Çarpım: "+ str(s1*s2))
        elif islem == "/":
            print("Bölüm: "+ str(s1/s2))
        elif islem == "!":
            n += 1
            print("Programdan çıkış yaptınız...")
        else:
            print("Hatalı Giriş! Bir işlem operatörü ya da (!) girmelisiniz. ")
            n += 1
        if islem != "!" and n == 0:
            s1 = input("Birinci sayıyı giriniz: ")
            s2 = input("İkinci sayıyı giriniz: ")
    else:
        print("Hatalı Giriş! Bir sayı girmelisiniz.")
        n +=1
   

    

    

    
    
              
    

