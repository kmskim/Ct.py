finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    max = len(array) -1
    min = 0
    geuss_target = len(array)//2
    
    while (min<=max): 
        if array[geuss_target] == target: 
            return True
        elif array[geuss_target] >= target:
             max = geuss_target -1 
        elif array[geuss_target] <= target:
             min = geuss_target +1  
        geuss_target = (max +min) //2
    return False
 # 내코드   
    # mid = len(array) // 2
    # while(True):
    #     if array[mid] == target:
    #         return True
    #     else:
    #         if array[mid] > target:
    #             mid = mid+len(array)/2
    #         else:
    #             mid= (mid + target)// 2
    # return False
result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)