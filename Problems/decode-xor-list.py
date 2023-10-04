def decode(encoded, first) :
        arr = [first]
        for i in encoded:
                arr.append(arr[-1]^i)
        return arr

print(decode([1,2,3],1))