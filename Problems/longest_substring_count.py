def lengthOfLongestSubstring( s: str) -> int:
        
        sub_str = s[0] 
        for char in s[1:]:
            if char == sub_str[0]:
               
                sub_str = sub_str.replace(char,"")
                sub_str += char
                
            elif char not in sub_str[1:]:
                sub_str += char
               

        return len(sub_str)

print(lengthOfLongestSubstring("abcabcbb"))