"""4 haneli bir şifre dediğiniz için şifrenin rakamlardan oluşması gerektiğini düşündüm.
    bu yüzden isdigit ile bunun kontrolünü yaptım. Kullanıcı rakam dışında bir giriş
    yaptığında hata vermesini sağladım
    """
# This script asks the user for the password and continues asking until the password is 4 digits. After, it presses on the screen

sifre = input("Enter your password: ")

while(len(sifre) != 4 and sifre.isdigit()):
    sifre = input("Enter your password: ")
    
if sifre.isdigit() == False:
    print("ERROR!")
elif len(sifre) == 4:
        print("Your password" , sifre)

    

        
