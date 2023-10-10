while True:
    user_input = input("Please enter two words: ")
    if not user_input or user_input == 'done':
        print("bye ;)")
        break
    words = user_input.split()
    if len(words) != 2:
        print("Please enter exactly TWO words!!!")
    else:
        word1, word2 = words
        if word1 < word2:
            print(f"{word1} comes first")
        elif word2 < word1:
            print(f"{word2} comes first")
        else:
            print("Both words are the same.")
