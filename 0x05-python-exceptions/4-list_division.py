#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_List = []
    for idx in range(list_length):
        div = 0
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
        finally:
            new_List.append(div)
    return new_List
