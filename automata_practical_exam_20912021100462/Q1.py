def is_divisible_by_3(input_string):
    state = 0
    for char in input_string:
        if char == '1':
            state = (state + 1) % 3
    return state == 0

while True:
    input_string = input("Enter a binary string (or 'exit' to quit): ")
    
    if input_string.lower() == 'exit':
        break
        
    if all(char in '01' for char in input_string):
        if is_divisible_by_3(input_string):
            print("The number of 1's is divisible by 3")
            state = 0
            print(f"Start State: {state}")
            for index, char in enumerate(input_string):
                next_state = (state + 1) % 3 if char == '1' else state
                if state == next_state:
                    print(f"Input = '{char}'")
                    print(f"Stay at state {state}")
                else:
                    print(f"Input = '{char}'")
                    print(f"Move from state {state} to state {next_state}")
                state = next_state
        else:
            print("The number of 1's is NOT divisible by 3")
    else:
        print("Invalid input") 