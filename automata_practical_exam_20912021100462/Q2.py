def check_ab():

    text = input("Enter a string of a's and b's (example: aabb): ")
    if not text:
        print("Rejected (Empty input)")
        return

    stack = ['$']  # Stack starts with a special bottom marker
    count_a = 0

    # Push all 'a's onto the stack
    for char in text:
        if char == 'a':
            count_a += 1
            stack.append('a')
        else:
            break  # Stop counting 'a's once a different character appears

    # Pop one 'a' for each 'b'
    valid = True
    for char in text[count_a:]:
        if char == 'b' and len(stack) > 1:
            stack.pop()
        else:
            valid = False
            break

    # Final check: only '$' must remain and a's should be > 0
    if valid and len(stack) == 1 and stack[0] == '$' and count_a > 0:
        print("Accepted")
    else:
        print("Rejected")


def check_parentheses():
    text = input("Enter parentheses string (example: ()()): ")
    if not text:
        print("Rejected (Empty input)")
        return

    stack = ['$']  # Stack starts with a special bottom marker

    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) <= 1:  # No matching '('
                print("Rejected")
                return
            stack.pop()
        else:
            print("Rejected (Invalid character)")
            return

    if len(stack) == 1 and stack[0] == '$':
        print("Accepted")
    else:
        print("Rejected")


# Menu interface
while True:
    print("\n--- PDA Simulation Menu ---")
    print("1. Check Balanced Parentheses ()")
    print("2. Check aⁿbⁿ")
    print("3. Exit")

    choice = input("Your choice (1-3): ")

    if choice == '1':
        check_parentheses()
    elif choice == '2':
        check_ab()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")