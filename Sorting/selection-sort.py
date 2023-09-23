def selection_sort(a_list):
    for fill in range(len(a_list)-1,0,-1):
        pos_of_max = 0
        for i in range(1,fill+1):
            if a_list[i] > a_list[pos_of_max]:
                pos_of_max = i

        a_list[fill],a_list[pos_of_max] = a_list[pos_of_max],a_list[fill]


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)