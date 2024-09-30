num_human = int(input("how many want participate :"))
Horror = 0
Romance = 0
Comedy = 0
History = 0
Adventure = 0
Action = 0
for i in range(num_human):
    for j in range(3):
        choose = int(
            input(
                "choose 1 genre between( 1:horror , 2:romance , 3:comedy , 4:history,5:adventure , 6:action ):"
            )
        )
        if choose == 1:
            Horror += 1
        elif choose == 2:
            Romance += 1
        elif choose == 3:
            Comedy += 1
        elif choose == 4:
            History += 1
        elif choose == 5:
            Adventure += 1
        elif choose == 6:
            Action += 1


print(
    "Horror:{}\nRomance:{}\nComedy:{}\nHistory:{}\nAdventure:{}\nAction:{}".format(
        Horror, Romance, Comedy, History, Adventure, Action
    )
)
