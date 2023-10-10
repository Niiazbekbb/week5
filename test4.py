while True:
    user_input = input("Please enter a string (or 'done' to finish): ")
    if user_input == 'done':
        print(" bye ;)")
        break
    special_characters = [',', '.', ':', '!', '?']
    converted_string = ''.join(char for char in user_input if char not in special_characters)
    converted_string = converted_string.upper()
    print( converted_string)
