s = "The AI and the ai are great"

def words_length_grouping(words):
    words_lengt={}
    for word in words:
        lenth_of_the_word= len(word)
        if lenth_of_the_word not in words_lengt:
            words_lengt[lenth_of_the_word]=[]
            
        words_lengt[lenth_of_the_word].append(word)
            
    return words_lengt
        
        
words= ["ai", "code", "brain", "xai", "go", "think", "do"]        
print(words_length_grouping(words))


# to check how many numbers of the same alphabet or other characters are there in the string 
s = "The AI and the ai are great"
def word(str):
    letters_count={}
    lower_case= str.lower()
    for letter in lower_case:
        if letter != " ":
            letters_count[letter]=letters_count.get(letter,0)+1
         
         
    return letters_count   
        
        
