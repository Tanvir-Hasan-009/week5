while True:
    user_input = input("Enter a string: ")

    if user_input == 'done':
        print("Bye!")
        break
    num_count= 0
    upper_count = 0
    lower_count = 0
    other = 0
    for char in user_input:
        if char.isupper():
            upper_count += 1
        elif char.isdigit():
            num_count += 1
        elif char.islower():
            lower_count += 1
        else:
            other += 1
        
    print("Upper letters:", upper_count)
    print("Lower letters:", lower_count)
    print("Num:", num_count)
    print("Other characters:", other)
    