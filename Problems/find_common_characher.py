def commonChars(words) :
        out = []
        
        for c in set(words[0]):
            c_common_cnt = min([w.count(c) for w in words])
            if c_common_cnt > 0:
                out += [c] * c_common_cnt

        return out

print(commonChars(["bella","label","roller"]))