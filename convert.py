def main():
    print("This program converts Celsius to Fahrenheit")
    print("Celsius temperature \t Fahrenheit Equivalent")
    for CelsiusTemp in range(0,101,10):
        FahrenheitTempEquivalent = ( 9 / 5 ) *CelsiusTemp + 32
        print(CelsiusTemp,"°C","\t\t\t",FahrenheitTemp,"°F")
    uc = input("Do you want to convert C to F (C) or F to C (F) or quit(Q)?:")
    while uc !='q':
        if uc == 'c':
            ctf()
            uc = input("Do you want to convert F to C (F) or quit(Q)?: ")
        elif uc == 'f':
            ftc()
            uc = input("Do you want to convert C to (F) or quit(Q)?: ")
        elif uc !='c' and uc !='f':
            print("Please make sure the input is valid.")
            uc = input("Do you want to convert C to F(C) or F to C(F) or quit(Q)?: ")
    print("exiting...")

main()