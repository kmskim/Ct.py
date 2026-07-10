finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
                #0 1 2 3 4 5 6
def is_exist_target_number_binary(target, array):
    max = len(array) -1
    min = 0
    geuss_target = len(array)//2
    array.sort()

    while min <= max:
            if  array[geuss_target] == target:
                return True
            elif array[geuss_target] >= target:
                max = geuss_target-1
            elif array[geuss_target] <= target:
                min = geuss_target+1
            geuss_target = (min + max) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
