try:
    input_apartments = int(input("Enter the quatriplegic: "))
    passability = True
    floors = 0
    if input_apartments >= 430: passability = False

    if passability is True and input_apartments <=287:
        if input_apartments <= 11:
            print(f"Apartment: {input_apartments}\nFloor: 2\nSection: 1")
        else:
            floors = input_apartments // 12
            floors += 2
            print(f"Apartment: {input_apartments}\nFloor: {floors}\nSection: 1")
    if passability is True and input_apartments >=288:
        if input_apartments <= 293:
            print(f"Apartment: {input_apartments}\nFloor: 2\nSection: 2")
        else:
            floors = input_apartments // 6
            floors -= 46
            print(f"Apartment: {input_apartments}\nFloor: {floors}\nSection: 2")
    if passability is False:
        print("The most recent apartment is 430.")
except:
    print("You entered the wrong thing")
