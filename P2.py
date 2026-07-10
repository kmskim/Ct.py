def find_not_repeating_first_character(string):
     
    # 이 부분을 채워보세요!
    answer = find_alphbat(string)
    return answer

def find_alphbat(string):
    array = [0] *26
    result = '_';

    for i in string:
        array[ord(i) - ord('a')] +=1

    for i in string:
        if array[ord(i) - ord('a')] == 1:
            return i;

    return result


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))