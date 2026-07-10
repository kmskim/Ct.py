# 소수 구하기
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

# input = 20
# def find_prime_list_under_number(number):
#     result = []
#     for i in range(2,number):
#         if identipy_number(i):
#             result.append(i)         
#     return result

# def identipy_number(number):
#     for i in range(2,number-1):
#         if number / i == 0:
#             return 0
#     return 1 

# result = find_prime_list_under_number(input)
# print(result)

#문자열 뒤집기
#Q. 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

# 예를 들어 S=0001100 일 때,
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.



#연속된 숫자 찾기 (0이 많은지 1이 많은지 판단)      1101010100101   1이7개 0이 6개
# 연속된 숫자가 없으면 하나씩 뒤집기
# target에 0 or1 target이랑 비교후 반환 같으면 continue 
# # 0,1 위치판단


#처음수 0인지 1인지 판별
#문자열만큼 반복
#앞뒤 비교후 뒤에가 1이면 1카운터에 +1
#		          0이면 0카운터에 +1

#둘중 작은거 찾기



input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_count = 0
    one_count = 0

    if string[0] == "0":
        zero_count+=1
    else:
        one_count+=1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                zero_count+=1
            else:
                one_count+=1

    return min(zero_count, one_count)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

