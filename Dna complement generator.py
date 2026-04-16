base = input("Enter DNA base: ")

if base == "A":
    print("T")
else:
    if base == "T":
        print("A")
    else:
        if base == "C":
            print("G")
        else:
            if base == "G":
                print("C")
            else:
                print("Invalid base")