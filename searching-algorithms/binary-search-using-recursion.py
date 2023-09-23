def binary_search(items,item):
    if len(items) == 0:
        return False
    else:
        mid = (0 + len(items)) //2
        if items[mid] == item:
            return True
        else:
            if item < items[mid]:
                return binary_search(items[:mid-1],item)
            else:
                return binary_search(items[mid+1:],item)


print(binary_search([1,2,3,4,5,6,7,8,9,10],5))