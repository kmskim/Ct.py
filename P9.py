# def factorial(n):
#     if n<=0: 
#         return 1
#     else:
#         return n * factorial(n-1);
# print(factorial(5))

input = "abcba"
         
def is_palindrome(string):
    # min = 0
    # max = len(string)-1
    # print(max)
    # for i in range(len(string)//2):
    #     if string[min] == string[max]:
    #         min+=1
    #         max-=1
    #     else: 
    #         return False
    if string[0] != string[-1]:
        return False
    elif len(string) <= 1:
        return True

    
    return is_palindrome(string[1:-1])

print(is_palindrome(input))