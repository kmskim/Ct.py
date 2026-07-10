array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    point_a=0
    point_b=0
    point =0
    result = [0]*(len(array1) + len(array2))   #8

    while point_a < (len(array1)) and point_b < (len(array2)):
        if array1[point_a] <= array2[point_b]:
            result[point] = array1[point_a]
            point_a+=1  
        else:
            result[point] = array2[point_b]
            point_b+=1
        point+=1

    if(point_a >= len(array1)):
        for i in range(point_b, len(array2)):
            result[point] = array2[i]
            point+=1
    else:   
        for i in range(point_a, len(array1)):
            result[point] = array1[i]
            point+=1
    
    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))