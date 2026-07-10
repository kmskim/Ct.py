# BOJ 1158

def josephus_problem(n, k):
    point =k-1;
    array = [0] *n
    answer = []
  
    for i in range(n):
        array[i] = i+1

        
    while len(answer) != n:
        answer.append(array.pop(point))     #2
        if len(array) != 0:
            point = (point + (k-1))%len(array)  #1

    print("<" + ", ".join(map(str, answer)) + ">") #3
n, k = map(int, input().split())
josephus_problem(n, k)

# def josephus_problem(n, k):
#     result_arr = []

#     next_index = k - 1
#     people_arr = list(range(1, n + 1))

#     while people_arr:
#         result = people_arr.pop(next_index)
#         result_arr.append(result)
#         if len(people_arr) != 0:
#             next_index = (next_index + (k - 1)) % len(people_arr)

#     print("<", ", ".join(map(str, result_arr)), ">", sep='')


# n, k = map(int, input().split())
# josephus_problem(n, k)