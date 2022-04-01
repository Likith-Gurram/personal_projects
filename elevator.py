#when executing only use y

state = [" "]*10
def display_state(state,floor):
    print(f"9|-->  {state[9]}  ")
    print(f"8|-->  {state[8]}  ")
    print(f"7|-->  {state[7]}  ")
    print(f"6|-->  {state[6]}  ")
    print(f"5|-->  {state[5]}  ")
    print(f"4|-->  {state[4]}  ")
    print(f"3|-->  {state[3]}  ")
    print(f"2|-->  {state[2]}  ")
    print(f"1|-->  {state[1]}  ")
    print(f"G|-->  {state[0]}  ")


def same_floor_check(floor, constant):# will return if True if the elevator is same floor as requested by the user
    return constant == floor

def floor_counter(constant, floor): #to check if same floor
    if constant == floor :
        return " "
    elif constant>floor: # if lower floor than requested it will go down a floor and print at a time
        for i in range(floor, constant):
            print(f"Moving down from floor {constant} to {floor}")
            constant -=1 #if i was used it creates from 0 to next number so instead used this to compensate a reverse range function which was not working
    elif constant<floor: # if higher floor than requested it will go up a floor and print at a time
        for i in range(constant, floor):
            print(f"Moving up from floor {i} to {floor}")


use_el = True
constant = 0 # storing the value to refer it and compare later
while use_el:
    print(f"The elevator is at the {constant} floor at the moment")
    choice = input("Do you need to use the elevator? ").lower()
    if choice == "y":
            floor = int(input("Enter a floor to go to"))
            if floor > 9 or floor < 0 :
                 print("there is no such floor")
                 break #solved the wrong number attempt

            if not same_floor_check(floor, constant):
                floor_counter(constant, floor)
                state[floor] = 'DING DING!'
                display_state(state, floor)
                state[floor] = " " # to clear out the space and make it visible for next user
                constant = floor
            else:
                print("You are already on same Floor bud! ")
    else:
        use_el = False
