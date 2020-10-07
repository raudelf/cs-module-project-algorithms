'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # Sort the incoming array
    arr.sort()

    # Create an empty array
    temp_array = []

    # Create a for loop to run through the arr
    for n in arr:
        # Check temp array if it contains the number
        if n in temp_array:
            # if it does, pop it out!
            temp_array.pop()
        else:
            # otherwise add it in!
            temp_array.append(n)

    return temp_array[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [3, 1, 1, 4, 5, 5, 3, 4, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
