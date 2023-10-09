while True:
    User_input = input("Please_enter_two_words: ")
    
    if User_input == "done":
        print("Bye!")
        break

    if ' ' not in User_input:
        continue

    words = User_input.split()

    word1, word2 = words
    if word1 > word2:
        Output = word2
    else:
        Output = word1

    print(f"{Output} comes first.")