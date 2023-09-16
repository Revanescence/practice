def reverse_list(numbers):
    return numbers[::-1]

def add_3_to_every_third_from_index(numbers, start_index):
    for i in range(start_index, len(numbers)):
        if (i - start_index) % 3 == 0:
            numbers[i] += 3
    return numbers

def subtract_7_from_every_5th_starting_from_index(numbers, start_index):
    for i in range(start_index, len(numbers), 5):
        numbers[i] -= 7
    return numbers

# Input the number of test cases
T = int(input("Enter the number of test cases (1 <= T <= 25): "))

# Check if T is within the specified range
if 1 <= T <= 25:
    # Process each test case
    for _ in range(T):
        # Read the length of the list
        L = int(input("Enter the length of the list (8 <= L <= 50): "))
        
        # Check if L is within the specified range
        if 8 <= L <= 50:
            while True:
                # Read the space-separated numbers as a string
                numbers_str = input(f"Enter {L} numbers separated by space: ")
                
                # Split the string and convert it to a list of integers
                numbers = list(map(int, numbers_str.split()))
                
                # Check if the number of entered values matches the specified list length
                if len(numbers) == L:
                    break  # Continue if the length matches
                else:
                    print(f"Please enter exactly {L} numbers.")
            
            # Check if each number in the list is within the range -100 to 100
            valid_numbers = all(-100 <= num <= 100 for num in numbers)
            
            if valid_numbers:
                # Reverse the list of numbers
                reversed_numbers = reverse_list(numbers)
                
                # Print the reversed list
                print("Reversed list:", *reversed_numbers)
                
                # Start changing numbers from a specific index (e.g., index 3)
                start_index = 3
                modified_numbers = add_3_to_every_third_from_index(numbers, start_index)
                
                # Print the modified list
                print("add_3_to_index_numbers_3:", *modified_numbers)
                
                # Subtract 7 from every 5th number starting from a specific index (e.g., index 5)
                start_index = 5
                final_numbers = subtract_7_from_every_5th_starting_from_index(numbers, start_index)
                
                # Print the final modified list
                print("subtract_7_from_index_numbers_5:", *final_numbers)
            else:
                print("Each number in the list must be between -100 and 100.")
        else:
            print("The length of the list must be between 8 and 50.")
else:
    print("The number of test cases must be between 1 and 25.")