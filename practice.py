# Function to reverse a list of numbers
def reverse_list(numbers):
    return numbers[::-1]

# Input the number of test cases
T = int(input("Enter the number of test cases (1 <= T <= 25): "))

# Check if T is within the specified range
if 1 <= T <= 25:
    # Process each test case
    for _ in range(T):
        # Read the length of the list
        N = int(input("Enter the length of the list (8 <= N <= 50): "))
        
        # Check if N is within the specified range
        if 8 <= N <= 50:
            # Read the space-separated numbers as a string
            numbers_str = input("Enter the numbers separated by space: ")
            
            # Split the string and convert it to a list of integers
            numbers = list(map(int, numbers_str.split()))
            
            # Check if each number in the list is within the range -100 to 100
            valid_numbers = all(-100 <= num <= 100 for num in numbers)
            
            if valid_numbers:
                # Reverse the list of numbers
                reversed_numbers = reverse_list(numbers)
                
                # Print the reversed list
                print(*reversed_numbers)
            else:
                print("Each number in the list must be between -100 and 100.")
        else:
            print("The length of the list must be between 8 and 50.")
else:
    print("The number of test cases must be between 1 and 25.")