import random
import names
choice = input("Яке ім'я ви хочете вибрати?\n 1 - чоловіче\n 2 - жіноче\n 3 - будь-яке\n")
if choice == "1":
    print(names.mnames[random.randint(0,20)])
elif choice == "2":
    print(names.wnames[random.randint(0, 20)])
elif choice == "3":
    name = names.mnames + names.wnames
    print(name[random.randint(0, 40)])