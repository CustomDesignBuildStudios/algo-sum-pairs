def sum_pairs(array_numbers, sum_number):
    array_of_sums = []
    for first_number in range(len(array_numbers)):
        for second_number in range(first_number,len(array_numbers),1):
            if array_numbers[first_number] + array_numbers[second_number] == sum_number:
                array_of_sums.append([array_numbers[first_number],array_numbers[second_number]])
    if len(array_of_sums) > 0:
        return array_of_sums
    else:
        return 'unable to find pairs'
