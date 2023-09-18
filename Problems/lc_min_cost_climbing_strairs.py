def min_cost(cost):
    costp = 0
    i = 0

    while i < len(cost)-1:
        if cost[i] < cost[i+1]:
            costp += cost[i]
            i+=1
        else:
            costp += cost[i+1]
            i+=2

    return costp




print(min_cost([0,2,2,1]))
