pswd_real = "ajax415"
pswd_user = ""

while pswd_user != pswd_real:
    pswd_user = input("contraseña: ")

    if pswd_user != pswd_real:
        print("incorrecta")

print("contraseña correcta")