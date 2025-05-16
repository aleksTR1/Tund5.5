def linnad():
    linnad = []
    elanikud = []
    
    n = int(input("Mitu linna soovid sisestada? "))
    for i in range(n):
        linn = input(f"Sisesta linna nimi #{i+1}: ").strip()
        elanike_arv = int(input(f"Sisesta elanike arv linnas {linn}: "))
        linnad.append(linn)
        elanikud.append(elanike_arv)
    
    while True:
        print("\nValikud:")
        print("1 - Elanike arv linna järgi")
        print("2 - Näita linnad ja elanike arvud tähestiku järjekorras")
        print("3 - Leia linn lähima elanike arvuga")
        print("4 - Linnad, kus elanike arv on väiksem kui n")
        print("5 - Välju")
        valik = input("Tee valik: ").strip()
        
        if valik == '1':
            linn = input("Sisesta linna nimi: ").strip()
            if linn in linnad:
                indeks = linnad.index(linn)
                print(f"Linnas {linn} elab {elanikud[indeks]} inimest.")
            else:
                print("Linna ei leitud.")
        
        elif valik == '2':
            linnad_sort = sorted(zip(linnad, elanikud))
            for linn, elanike_arv in linnad_sort:
                print(f"{linn}: {elanike_arv}")
        
        elif valik == '3':
            siht_arv = int(input("Sisesta elanike arv, millega võrrelda: "))
            erinevused = [abs(el - siht_arv) for el in elanikud]
            min_index = erinevused.index(min(erinevused))
            print(f"Lähim elanike arvuga linn on {linnad[min_index]}: {elanikud[min_index]} elanikku.")
        
        elif valik == '4':
            piir = int(input("Sisesta maksimaalne elanike arv: "))
            väiksemad = [(l, e) for l, e in zip(linnad, elanikud) if e < piir]
            if väiksemad:
                for l, e in väiksemad:
                    print(f"{l}: {e}")
            else:
                print("Selliseid linnu pole.")
        
        elif valik == '5':
            print("Head aega!")
            break
        
        else:
            print("Vale valik, proovi uuesti.")

if __name__ == "__main__":
    linnad()
