def short_bubble_sort(a_list):
    exchange = True
    pos = len(a_list) - 1

    while pos > 0 and exchange:
        exchange = False
        for i in range(pos):
            if  a_list[i] > a_list[i+1]:
                exchange =True
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]

        pos -=1

a_list = [20,30,40,90,50,60,70,80,100,110]
short_bubble_sort(a_list)
print(a_list)