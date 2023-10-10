user_input = input("Please enter a string: ")
print(f"Input string = {user_input}")
index = len(user_input) - 1  
while index >= 0:
    print(user_input[index])
    index -= 1
