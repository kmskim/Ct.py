shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 이중for문 그냥 작성
# def is_available_to_order(menus, orders):
#     count = len(orders)
#     for i in menus:
#         for j in orders:
#             if  i == j:
#                 count-=1
#     if count>0:
#         return False
#     return True


# result = is_available_to_order(shop_menus, shop_orders)
# print(result)

# 이분법 정렬
def is_available_to_order(menus, orders):
    # menus.sort()
    # orders.sort()
    # while len(orders) !=0: 
    #     count=0
    #     target = orders.pop(0)
    #     for i in menus:
    #         if i != target:
    #             count =1
    #     if count ==0:
    #         return False
    
    menu_set = set(menus)   #set의 자료구조: set은 중복을 허용하지 않는 집합(Set) 자료형입니다.
    for order in orders:
        if order not in menu_set:   #not in: 포함되어 있지 않으면 True
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)

#Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.