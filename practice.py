# for word 

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

# for sentence 


def unRepeted_sent(sentences):
    no_of_each_Sentence= {}
    
    for x in sentences:
        no_of_each_Sentence[x] = no_of_each_Sentence.get(x, 0) + 1 
        
        
    for y in no_of_each_Sentence:
        if no_of_each_Sentence[y] ==1 :
            return y
    
    return "no sentences like that "
    
    
sentences=["AI is powerful", "We love coding", "AI is powerful", "Humans teach machines", "We love coding"]
result=unRepeted_sent(sentences)
print(result)

# for frequent words 
def frequent_Words(sentences , stop_words):
    count={}
    for n in sentences:
        words = n.lower().split()
        for word in words:
            if word not in stop_words:
                count[word] = count.get(word, 0) +1 
                
                
            
    max=0
    most_frequent_word= None
    for word in count:
        if count[word]>max:
            max= count[word]
            most_frequent_word= word 
            
    return most_frequent_word

sentences = [
    "AI is the future",
    "The future is bright",
    "AI helps humans",
    "Humans and AI together"
]

stop_words = ["is", "the", "and"]

print(frequent_Words(sentences, stop_words))
