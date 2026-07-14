all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}   
    for key in all_array:  # all_array의 key를 dict에 넣습니다
        dict[key] = True
    
    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # dict에 남아있는 key가 결석한 학생입니다
        return key

print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))