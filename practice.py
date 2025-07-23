def first_non_repeating(str):
    char_count= {}
    for x in str:
        char_count[x] = char_count.get(x, 0)+1
        
    for char in char_count:
        if char_count[char] == 1:
            return char
            
    return "_"
x= "mmacha"
print(first_non_repeating(x))

#output c
