def sequential_search(a_list,item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        pos+=1

    return found

print(sequential_search([1,2,3,4,5],6))
