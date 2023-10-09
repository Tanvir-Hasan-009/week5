while True:
    user_input = input("Enter a string (type 'done' to exit): ")
    if user_input == 'done':
        print("Bye!")
        break
    special_chars = set(":,.;!")
    output = ''
    for char in user_input:
        if char not in special_chars:
            output += char.upper()
    print("Final string:", output)