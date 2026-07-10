
numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []

# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

#-1+1+1+1+1 = 3
#+1-1+1+1+1 = 3
#+1+1-1+1+1 = 3
#+1+1+1-1+1 = 3
#+1+1+1+1-1 = 3

# 2 3 1
#0              0                     0
# 1            +2                    -2
# 2          5     -1                 1    -5
# 3          6      0                 2      -4   
# IF 타겟이면 count up? 
#재귀
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    count =0
    Circle_get_count_of_ways_to_target_by_doing_plus_or_minus(array,0,0)
    
    for i in result:
        if i == target:
            count+=1
    return count

def Circle_get_count_of_ways_to_target_by_doing_plus_or_minus(array, Index, CurNum):
    if len(array) == Index:
        result.append(CurNum)
        return   
    Circle_get_count_of_ways_to_target_by_doing_plus_or_minus(array, Index+1, CurNum + array[Index])
    Circle_get_count_of_ways_to_target_by_doing_plus_or_minus(array, Index+1, CurNum - array[Index])


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  





