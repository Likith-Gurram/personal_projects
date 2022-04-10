state = [" "]*10
def display_state():
    '''
    This funtion displays the state of the elevator
    '''
    for i, floor in enumerate(state):
        floor_id = i if floor != 0 else 'G' 
        print(f"{floor_id}|--> {floor} ")


def same_floor_check(floor, curr_floor):
    '''
    This function returns True if the elevator is same floor as requested by the user
    '''
    return curr_floor == floor

def floor_counter(curr_floor, floor): 
    '''
    Check if same floor
    '''
    if same_floor_check(floor, curr_floor):
        return " "
    
    # If lower floor than requested it will go down a floor and print at a time
    elif curr_floor > floor:
        for i in range(floor, curr_floor):
            print(f"Moving down from floor {curr_floor} to {floor} ")
            # BUG!!!!: never update the variable you write in loop!!!!
            # Change this logic, this doesnt work for multiple floors
            curr_floor -= 1 #if i was used it creates from 0 to next number so instead used this to compensate a reverse range function which was not working
    
    elif curr_floor < floor: # if higher floor than requested it will go up a floor and print at a time
        for i in range(curr_floor, floor):
            print(f"Moving up from floor {i} to {floor} ")

def sanitize_floor(floor):
    ''' Check if entered floor is valid '''
    # This is to verify if the entered value is char or not.
    if not floor.isnumeric():
        print("You entered a character try again")
        return

    floor = int(floor) #as the input is taken as string first, it will convert to number and proceeed furthur.
    if (floor > 9 or floor < 0):
        print(f"there is no such floor as {floor}")
        return  # resolves the issue with exiting with a break statement

    return int(floor)
if __name__ == "__main__":
    curr_floor = 0 # storing the value to refer it and compare later
    while True:
        print(f"The elevator is at the {curr_floor} floor at the moment")
        choice = input("Do you need to use the elevator? [y/n]: ").lower()
        
        if choice == "y":
            floor = (input("Enter a floor to go to: "))
            floor = sanitize_floor(floor)

            if not floor: continue

            if same_floor_check(floor, curr_floor):
                print("You are already on same Floor bud!")
                continue
            
            floor_counter(curr_floor, floor)
            state[floor] = 'DING DING!'
            display_state()
            # This ensures the DING DING is removed everytime it has given the result.
            # Or else it causes the the DING to remain
            state[floor] = " "
            curr_floor = floor

        elif choice == "n":
            print("Thank you for using the elevator")
            break
        else:
            print("You entered something wrong, valid options are [y/n]")
            continue
