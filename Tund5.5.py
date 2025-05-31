def pood():
    ostud = []
    hinnad = []
    ostetud = []
    n = int(input("Mitu toodet soovid lisada? "))
    for i in range(n):
        toode = input(f"{i+1}. Sisesta toote nimi: ").strip()
        hind = float(input(f"   Sisesta toote '{toode}' hind: "))
        ostud.append(toode)
        hinnad.append(hind)
    while True:
        print("\nVALIKUD:")
        print("1 - Eemalda ostetud toode ja näita tšekk")
        print("2 - Näita ostunimekirja tähestiku järgi")
        print("3 - Kalleim ja odavaim toode")
        print("4 - Leia toote hind nime järgi")
        print("5 - Välju")
        valik = input("Tee valik (1-5): ").strip()
        if valik == "1":
            toode = input("Sisesta ostetud toode: ").strip()
            if toode in ostud:
                idx = ostud.index(toode)
                ostetud.append((ostud.pop(idx), hinnad.pop(idx)))
                print("Toode ostetud!")
                summa = sum(h for _, h in ostetud)
                print("\nTšekk:")
                for t, h in ostetud:
                    print(f"{t} - {h:.2f}€")
                print(f"Kokku: {summa:.2f}€")
            else:
                print("Toodet ei leitud!")
        elif valik == "2":
            for toode, hind in sorted(zip(ostud, hinnad)):
                print(f"{toode}: {hind:.2f}€")
        elif valik == "3":
            if ostud:
                max_idx = hinnad.index(max(hinnad))
                min_idx = hinnad.index(min(hinnad))
                print(f"Kalleim: {ostud[max_idx]} - {hinnad[max_idx]:.2f}€")
                print(f"Odavaim: {ostud[min_idx]} - {hinnad[min_idx]:.2f}€")
            else:
                print("Pole ühtegi toodet.")
        elif valik == "4":
            nimi = input("Sisesta toote nimi: ").strip()
            if nimi in ostud:
                idx = ostud.index(nimi)
                print(f"{nimi} maksab {hinnad[idx]:.2f}€")
            else:
                print("Toodet ei leitud.")
        elif valik == "5":
            print("Head ostlemist!")
            break
        else:
            print("Vigane valik, proovi uuesti.")
if __name__ == "__main__":
    pood()









def magazin():
    pokupki = []
    tseny = []
    kupil = []
    n = int(input("Сколько товаров вы хотите добавить? "))
    for i in range(n):
        tovar = input(f"{i+1}. Введите название товара: ").strip()
        tsena = float(input(f"   Введите цену для товара '{tovar}': "))
        pokupki.append(tovar)
        tseny.append(tsena)
    while True:
        print("\nМЕНЮ:")
        print("1 - Удалить купленный товар и показать чек")
        print("2 - Показать список покупок по алфавиту")
        print("3 - Самый дорогой и самый дешёвый товар")
        print("4 - Найти цену по названию товара")
        print("5 - Выйти")
        vibor = input("Выберите пункт (1-5): ").strip()
        if vibor == "1":
            tovar = input("Введите купленный товар: ").strip()
            if tovar in pokupki:
                i = pokupki.index(tovar)
                kupil.append((pokupki.pop(i), tseny.pop(i)))
                print("Товар куплен!")
                summa = sum(c for _, c in kupil)
                print("\nЧек:")
                for t, c in kupil:
                    print(f"{t} - {c:.2f}€")
                print(f"Итого: {summa:.2f}€")
            else:
                print("Товар не найден!")
        elif vibor == "2":
            for t, c in sorted(zip(pokupki, tseny)):
                print(f"{t}: {c:.2f}€")
        elif vibor == "3":
            if pokupki:
                max_i = tseny.index(max(tseny))
                min_i = tseny.index(min(tseny))
                print(f"Самый дорогой: {pokupki[max_i]} - {tseny[max_i]:.2f}€")
                print(f"Самый дешёвый: {pokupki[min_i]} - {tseny[min_i]:.2f}€")
            else:
                print("Список покупок пуст.")
        elif vibor == "4":
            name = input("Введите название товара: ").strip()
            if name in pokupki:
                i = pokupki.index(name)
                print(f"{name} стоит {tseny[i]:.2f}€")
            else:
                print("Товар не найден.")
        elif vibor == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    magazin()
