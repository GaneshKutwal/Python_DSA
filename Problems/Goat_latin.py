def toGoatLatin(sentence: str) -> str:
        word_l = sentence.split()
        cnt = 0
        vowel = "aeiouAEIOU"
        while cnt < len(word_l):
            
            for ele in vowel:
                if word_l[cnt][0] == ele:
                    word_l[cnt] += "ma"
                    break
            else:
                word_l[cnt] = word_l[cnt][1:] + word_l[cnt][0] + "ma"

            word_l[cnt] += "a"*(cnt+1)
            cnt+=1
        return " ".join(word_l)
        
print(toGoatLatin("I speak Goat Latin"))