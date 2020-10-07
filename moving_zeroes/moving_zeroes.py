'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    # Create two arrays, the zero array and other array
    zero_array = []
    other_array = []

    # Create a for loop to run through the arr
    for n in arr:
        # Check to see if n is 0
        if n == 0:
            # Add it to the zero list if so
            zero_array.append(n)
        else:
            # Otherwise add it to to other list
            other_array.append(n)
    return other_array + zero_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
