def summaryRanges(nums) :
        res = []

        for i,num in enumerate(nums):
            if res and res[-1][1] == num -1:
                res[-1][1] = num
            else:
                res.append([num,num])

        return [str(x) if x==y else str(x)+"->"+str(y) for x,y in res]
        
            

print(summaryRanges([0,1,2,3,5,6,8,9]))