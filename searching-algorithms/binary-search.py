def binary_search(a_list,item):
    low = 0
    high = len(a_list) - 1
    
    found = False

    while low < high and not found:
        mid = (high + low) // 2
        if a_list[mid] == item:
            found = True
        else:
            if item < a_list[mid]:
                high = mid -1
            else:
                low = mid + 1

    return found



print(binary_search([1,2,3,4,5,6,7,8,9,10],12))