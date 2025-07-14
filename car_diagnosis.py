## A program to diagnose the problem with our car.

def car_diagnosis():
    starts = input("Does the car start? (Y/N): ").upper()
    if starts == 'Y':
        click_click = input("Does it make a click-click sound? (Y/N): ").upper()
        if click_click == 'Y':
            print("Diagnosis: Replace the battery.")
        else:
            turns_on_but_not_start = input("Does the car turn on but not start? (Y/N): ").upper()
            if turns_on_but_not_start == 'Y':
                print("Diagnosis: Check the spark plugs.")
            else:
                starts_then_stalls = input("Does the car start and then stall? (Y/N): ").upper()
                if starts_then_stalls == 'Y':
                    fuel_injection = input("Does the car have fuel injection? (Y/N): ").upper()
                    if fuel_injection == 'Y':
                        print("Diagnosis: Take the car to the workshop.")
                    else:
                        print("Diagnosis: Open and close the choke.")
                else:
                    print("Diagnosis: Could not determine the exact problem.")
    else:
        corroded_terminals = input("Are the battery terminals corroded? (Y/N): ").upper()
        if corroded_terminals == 'Y':
            print("Diagnosis: Clean the terminals and try starting again.")
        else:
            print("Diagnosis: Replace the cables and try starting again.")
            
            
car_diagnosis()
    