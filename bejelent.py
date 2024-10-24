f_nevek = []
jelszavak = []

with open("felhasználó.txt", "a", encoding="utf-8") as f:
    pass 

with open("felhasználó.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        parts = line.strip().split(";")
        if len(parts) == 2: 
            f_nevek.append(parts[0])
            jelszavak.append(parts[1])

def menu():
    while True:
        print("""  _____ ___       _     _       _   
 |  ___/_/_/ ___ | | __| | __ _| |_ 
 | |_ / _ \ / _ \| |/ _` |/ _` | (_)
 |  _| |_| | (_) | | (_| | (_| | |_ 
 |_|  \___/ \___/|_|\__,_|\__,_|_(_)\n""")
        print("""
    - 1. Bejelentkezés
    - 2. Regisztráció
    - 3.Regisztrált felhasználók
    - 4. Kilépés""")
        
        melyik = input("Válassz egy lehetőséget (1/2/3): ")

        if melyik == "1":
            bejelentkezes()
        elif melyik == "2":
            regisztracio()
        elif melyik == "3":
            reg_felh()
        elif melyik == "4":
            print("""  _  ___ _   __         __            
 | |/ (_) | /_/ _ __   /_/  ___       
 | ' /| | |/ _ \ '_ \ / _ \/ __|      
 | . \| | |  __/ |_) |  __/\__ \_ _ _ 
 |_|\_\_|_|\___| .__/ \___||___(_|_|_)
               |_|                    """)
            break
        else:
            print("Érvénytelen választás, kérlek válassz újra.")

def bejelentkezes():
    print("""  ____        _      _            _   _             __        
 | __ )  ___ (_) ___| | ___ _ __ | |_| | _____ ____/_/  ___ _ 
 |  _ \ / _ \| |/ _ \ |/ _ \ '_ \| __| |/ / _ \_  / _ \/ __(_)
 | |_) |  __/| |  __/ |  __/ | | | |_|   <  __// /  __/\__ \_ 
 |____/ \___|/ |\___|_|\___|_| |_|\__|_|\_\___/___\___||___(_)
           |__/      \n""")
    
    while True:
        nev = input("Írd be a felhasználónevedet (vagy 'quit' a kilépéshez): ")
        if nev.lower() == "quit":
            break

        if nev in f_nevek:
            index = f_nevek.index(nev)
            jelszo = input("Írd be a jelszavadat: ")
            if jelszavak[index] == jelszo:
                print(f"\nSikeres bejelentkezés, üdvözlünk {nev}!")
                break
            else:
                print("Hibás jelszó! Próbáld újra.")
        else:
            print("Nem létezik ilyen felhasználónév! Ha még nincs fiókod, regisztrálj.")

def regisztracio():
    print("""  ____            _         _         __       _   __   
 |  _ \ ___  __ _(_)___ ___| |_ _ __ /_/_  ___(_) /_/ _ 
 | |_) / _ \/ _` | / __|_  / __| '__/ _` |/ __| |/ _ (_)
 |  _ <  __/ (_| | \__ \/ /| |_| | | (_| | (__| | (_) | 
 |_| \_\___|\__, |_|___/___|\__|_|  \__,_|\___|_|\___(_)
            |___/                                       \n""")
    
    while True:
        felh_nev = input("Írd be a felhasználónevedet (vagy 'quit' a kilépéshez): ")
        
        if felh_nev.lower() == "quit":
            break
        if not (3 <= len(felh_nev) <= 15):
            print("A felhasználónévnek 3-15 karakter hosszúnak kell lennie!")
            continue

        if felh_nev in f_nevek:
            print("Ez a felhasználónév már foglalt! Próbálj meg egy másikat.")
        elif felh_nev not in f_nevek:
            while True:
                jelszo = input("Írd be a jelszavadat: ")

                if len(jelszo) < 6:
                    print("A jelszónak legalább 6 karakter hosszúnak kell lennie! Próbáld újra.")
                elif not any(char.isdigit() for char in jelszo):
                    print("A jelszód nem eléggé erős! Használj számokat is!")
                elif not any(char.isalpha() for char in jelszo):
                    print("A jelszód nem eléggé erős! Használj betüket is!")
                else:
                    jelszo2 = input("Erősítsd meg a jelszavadat: ")

                    if jelszo != jelszo2:
                        print("A jelszavak nem egyeznek! Próbáld újra.")
                    else:
                        with open("felhasználó.txt", "a", encoding="utf-8") as f:
                            f.write(felh_nev + ";" + jelszo + "\n")
                        
                        f_nevek.append(felh_nev)
                        jelszavak.append(jelszo)
                        print(f"\nSikeres regisztráció, {felh_nev}! Most már bejelentkezhetsz.")
                        menu()

def reg_felh():
    print("""  ____            _         _         __  _ _      __      _ _                           __  _   __  _      
 |  _ \ ___  __ _(_)___ ___| |_ _ __ /_/_| | |_   / _| ___| | |__   __ _ ___ _____ __   /_/_| | /_/ | | ___ 
 | |_) / _ \/ _` | / __|_  / __| '__/ _` | | __| | |_ / _ \ | '_ \ / _` / __|_  / '_ \ / _` | |/ _ \| |/ (_)
 |  _ <  __/ (_| | \__ \/ /| |_| | | (_| | | |_  |  _|  __/ | | | | (_| \__ \/ /| | | | (_| | | (_) |   < _ 
 |_| \_\___|\__, |_|___/___|\__|_|  \__,_|_|\__| |_|  \___|_|_| |_|\__,_|___/___|_| |_|\__,_|_|\___/|_|\_(_)
            |___/                                                                                           \n""")
    for felh in f_nevek:
        tovabb = input(f"""          - Felhasználó név: '{felh}', Jelszó: '###' """)
        if tovabb == "":
            continue

menu()
