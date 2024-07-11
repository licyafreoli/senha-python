while True:
    senhadigitada = str(input("digite sua senha:"))


    reqletraminuscula = "abcdefghijklmnopqrstuvwxyzçáàãâéèêíìóòõôúùûü"
    reqletramaiuscula = reqletraminuscula.upper()
    reqnumeros = "0123456789"

    temmaiuscula = 0
    temminuscula = 0
    temnumero = 0
    temcaraqterespecial = 0
    tem8digitos = 0

    if len(senhadigitada) >= 8:
        tem8digitos = 1

    for letradavez in senhadigitada:
        if letradavez in reqletraminuscula:
            temminuscula = 1
        elif letradavez in reqletramaiuscula:
            temmaiuscula = 1
        elif letradavez in reqnumeros:
            temnumero = 1
        else:
            temcaraqterespecial = 1

    totalatendidos = tem8digitos + temminuscula + temmaiuscula + temnumero + temcaraqterespecial

    if totalatendidos <= 2:
                print("sua senha é muito fraca")
    elif totalatendidos <= 4:
                print("sua senha não é boa o suficiente")
    else:
                print("sua senha é forte")
                break