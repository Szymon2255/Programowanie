filament = [150, 240, 175, 260, 195, 310, 225, 180, 275, 160]
print("Przed sortowaniem:", filament)

laczna_suma = sum(filament)
print("Łączna suma:", laczna_suma)

laczna_suma = 0
liczba_wydrukow = 5

i = 0
zamieniono = True

# Pętla zewnętrzna
while i < len(filament) - 1 and zamieniono:
    zamieniono = False
    j = 0
    # Pętla wewnętrzna
    while j < len(filament) - 1 - i:
        if filament[j] > filament[j + 1]:
            # Zamiana miejscami
            filament[j], filament[j + 1] = filament[j + 1], filament[j]
            zamieniono = True
        j += 1
    i += 1
    print("Po przejściu", i, ":", filament)

print("Po posortowaniu:", filament)


if liczba_wydrukow >= 4:
    print("Liczba wydruków wynosi 4")
    print("Opiekunowie powini oszczędzać filament")
else:
    print("Wszystko jest w normie")
