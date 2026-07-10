class Node:
    #첫번째 노드값 할당및 다음 노드 값 할당
    def __init__(self, data):   
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        #Node class 호출로 초기값 값할당
        self.head = Node(value)

    #다음 node값 할당
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    point =linked_list_1.head
    sum_1 = Sansu(point)
    
    point =linked_list_2.head
    sum_2 = Sansu(point)

    return sum_1+sum_2;

def Sansu(point):
    sum=0
    while point is not None:
        sum= sum*10 + point.data
        point = point.next
    return sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2)) 

