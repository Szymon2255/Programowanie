daneco2 = [750, 990, 1180, 1050, 820, 1300, 970]

prog = 1000

limit = 3


for stezenie in daneco2:
    if stezenie < prog:
        print(f"Stężenie CO2 wynosi {stezenie} – poniżej progu")
    elif stezenie > prog:
        print(f"Stężenie CO2 wynosi {stezenie} – powyżej progu")
    else:
        print(f"Stężenie CO2 wynosi {stezenie} – równe progowi")

    if prog > limit:
        print(input("Czy trzeba wywietrzyć?: "))
        
  


