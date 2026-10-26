pensje = [4200, 5100, 4800, 4500, 4700, 5300, 4900, 35000, 4400]
print("Przed sortowaniem:", pensje)
i = 0
zamieniono = True

while i < len(pensje) - 1 and zamieniono:
    zamieniono = False
    j = 0
    while j < len(pensje) - 1 - i:
        if pensje[j] > pensje[j + 1]:
            pensje[j], pensje[j + 1] = pensje[j + 1], pensje[j]
            zamieniono = True
        j += 1
    i += 1
    print("Po przejściu", i, ":", pensje)

print("Po posortowaniu:", pensje)

najnizsza = pensje[0]
najwyzsza = pensje[-1]
print(f"3. Najniższa pensja: {najnizsza}, Najwyższa pensja: {najwyzsza}")

srednia = sum(pensje) / len(pensje)
print(f"4. Średnia arytmetyczna: {srednia:.2f}")

rozstep = najwyzsza - najnizsza
n = len(pensje)
if n % 2 == 1:
    mediana = pensje[n // 2]
else:
    mediana = (pensje[n // 2 - 1] + pensje[n // 2]) / 2
print(f"5. Rozstęp: {rozstep}, Mediana: {mediana}")

ponizej_sredniej = sum(1 for p in pensje if p < srednia)
print(f"6. Liczba pracowników zarabiających poniżej średniej: {ponizej_sredniej}")