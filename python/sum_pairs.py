def sum_pairs(array_numbers, sum_number):
    """Sum Pairs
    Takes an array of numbers and a desired sum 
    Returns an array of all the two numbers that equals the desired sum.

    Parameters:
    array_numbers - array(numbers) - list of numbers to check
    sum_numbers   - number         - desired number
    """
    array_of_sums = []
    for first_number in range(len(array_numbers)):
        #Look for match ahead of current index
        for second_number in range(first_number,len(array_numbers),1):
            if array_numbers[first_number] + array_numbers[second_number] == sum_number:
                array_of_sums.append([array_numbers[first_number],array_numbers[second_number]])
    if len(array_of_sums) > 0:
        return array_of_sums
    else:
        return 'unable to find pairs'
