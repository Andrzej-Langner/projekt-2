def warehouse(name, quantity):
    all = name + "( + quantity + )"
    all
    return all

def go_out(s):
    if s == "": # Ekwiwalent nacisnięcia Entera
        return True

dt = {} # Pusty słownik

while True:
    print('nacisnij "Enter", aby zakonczyć wprowadzenie produktów.')
    name = input("nazwa: ")
    quantity = (input("Ilosc: "))

    if go_out(name) or go_out(quantity):
        print("Nie podano jednej wartosci")
        break

    dt[name] = quantity  # Tutaj zapełniamy słownik
    data = warehouse(name, quantity)
    print(f"\nStan: {data}")
    print(12)


print(dt)