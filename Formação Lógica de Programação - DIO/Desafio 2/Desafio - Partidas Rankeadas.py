
winQuantity = int(input("Type the number of victories: "))
loseQuantity = int(input ("Type the number of defeats: "))


def balanceOfGame(wins, loses):
    
    balance = wins - loses

    if (balance < 0):
        balance = -balance
        level = "Iron"
        status = "defeat(s)"
    elif(balance <= 10):
        level = "Iron"
        status = "win(s)"
    elif(balance <= 20):
        level = "Bronze"
        status = "win(s)"
    elif(balance <= 50):
        level = "Silver"
        status = "win(s)"
    elif(balance <= 80):
        level = "Gold"
        status = "win(s)"
    elif(balance <= 90):
        level = "Diamond"
        status = "win(s)"
    elif(balance <= 100):
        level = "Legendary"
        status = "win(s)"
    elif(balance > 100):
        level = "Immortal"
        status = "win(s)"
    else:
        print("Digite um valor válido")

    print(f"The hero have a balance of {balance} {status} and he/she is on {level} level")
        

balanceOfGame(winQuantity, loseQuantity)
