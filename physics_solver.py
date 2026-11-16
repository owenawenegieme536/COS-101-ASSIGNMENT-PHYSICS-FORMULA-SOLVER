# PHYSICS FORMULA SOLVER - VERSION 3
# Five different Physics calculations using a while loop.
# Answers are rounded to 2 decimal places.

while True:
    print("\n" + "=" * 40)
    print("       PHYSICS FORMULA SOLVER 3")
    print("=" * 40)
    print("1. Electric Charge")
    print("2. Ohm's Law (Resistance)")
    print("3. Frequency")
    print("4. Heat Energy")
    print("5. Efficiency")

    choice = input("Choose a formula (1-5): ").strip()

    if choice == "1":
        current = float(input("Enter current (A): "))
        time = float(input("Enter time (s): "))
        charge = current * time
        print(f"Electric Charge = {charge:.2f} C")

    elif choice == "2":
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        if current == 0:
            print("Current cannot be zero.")
        else:
            resistance = voltage / current
            print(f"Resistance = {resistance:.2f} ohms")

    elif choice == "3":
        cycles = float(input("Enter number of cycles: "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            frequency = cycles / time
            print(f"Frequency = {frequency:.2f} Hz")

    elif choice == "4":
        mass = float(input("Enter mass (kg): "))
        specific_heat = float(input("Enter specific heat capacity (J/kg°C): "))
        temperature_change = float(input("Enter temperature change (°C): "))
        heat = mass * specific_heat * temperature_change
        print(f"Heat Energy = {heat:.2f} J")

    elif choice == "5":
        useful_output = float(input("Enter useful energy output (J): "))
        total_input = float(input("Enter total energy input (J): "))
        if total_input == 0:
            print("Total input energy cannot be zero.")
        else:
            efficiency = (useful_output / total_input) * 100
            print(f"Efficiency = {efficiency:.2f}%")

    else:
        print("Invalid choice. Please select a number from 1 to 5.")

    again = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Thank you for using the Physics Formula Solver!")
        break
