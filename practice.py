def reverse_list(numbers):
    return numbers[::-1]

# Input the number of test cases
T = int(input("Enter the number of test cases (1 <= T <= 25): "))

# Check if T is within the specified range
if 1 <= T <= 25:
    # Process each test case
    for _ in range(T):
        # Read the length of the list
        N = int(input())
        
        # Read the list of numbers
        numbers = list(map(int, input().split()))
        
        # Reverse the list of numbers
        reversed_numbers = reverse_list(numbers)
        
        # Print the reversed list
        print(*reversed_numbers)
else:
    print("The number of test cases must be between 1 and 25.")