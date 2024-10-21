f_nevek = []
jelszavak = []

with open("Felhasználó.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        parts = line.strip().split(";")
        f_nevek.extend({
            parts[0],
        })

        jelszavak.extend({
            parts[1],
        })        

def menu():
    while True:
        print("-----Főoldal-----")
        melyik = input("""1.Bejelentkezés
2.regisztráció
3.Kilépés\n""")
        if melyik == "1":
            bejelentkezes()
        elif melyik == "2":
            regisztarcio()
        elif melyik == "3":
            break

def bejelentkezes():
    print("-----Bejelentkezés-----")

    while True:
        nev = input("Írd be a felhasználó nevedet:")
        
        if f_nevek.__contains__(nev):
            jelszo = input("Írd be a jelszavadat: ")
            if f_nevek.__contains__(jelszo):
                print("Sikeres bejelentkezés!")
            else:
                print("Heltelen jelszó!")
        else:
            print("Nem létezik ilyen felhasználónév! \nHa még nincsen fiókod regisztrálj!")
            
def regisztarcio():

    while True:

        print("-----Regisztráció-----")

        fel_nev = input("Írd be a felhasználó nevedet: ")
        if f_nevek.__contains__(fel_nev):
            print("Ez a felhasználó név már foglalt!")
        else:
            with open("Felhasználó.txt", "a", encoding="utf-8") as f:
                f.write("".join(fel_nev) + ";")
            
            jelszo = input("Írd be a jelszavadat: ")
            jelszo2 = input("Erősítsd meg a jelszavadat: ")

            if jelszo2 != jelszo:
                print("Nem egyezik meg a két jelszó!")
            elif jelszo == jelszo2:
                    with open("Felhasználó.txt", "a", encoding="utf-8") as f:
                        f.write("".join(jelszo) + "\n")
                        break

menu()