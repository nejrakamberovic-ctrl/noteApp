from func import zapisi, procitaj

while True:
    izbor = int(input("Uneiste izbor"))
    if izbor == 1:
        file_name = input("Ime fajla")
        tekst = input("Sta zapisati?")
        zapisi(file_name, tekst)
        print("Pisanje u fajl")
    elif izbor == 2:
        procitaj()
        print("Citanje iz fajla")
    elif izbor == 0:
        print("Bye")
        break
