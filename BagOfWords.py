def vectorize(tokens):
    ''' This function takes list of words in a sentence as input 
    and returns a vector of size of filtered_vocab.It puts 0 if the 
    word is not present in tokens and count of token if present.'''
    vector=[]
    for w in filtered_vocab:
        vector.append(tokens.count(w))
    return vector
def unique(sequence):
    '''This functions returns a list in which the order remains 
    same and no item repeats.Using the set() function does not 
    preserve the original ordering,so i didnt use that instead'''
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
stopwords=["to","is","a","now"]
sp=[",",":"," ",";",".","?"]
str1="Welcome to Great Learning , Now start learning"
str2="Learning is a good practice"
str1=str1.lower()
str2=str2.lower()
tokens1=str1.split()
tokens2=str2.split()
print(tokens1)
print(tokens2)
vocab=unique(tokens1+tokens2)
print(vocab)
filtered_vocab=[]
for w in vocab: 
    if w not in stopwords and w not in sp: 
        filtered_vocab.append(w)
print(filtered_vocab)
vector1=vectorize(tokens1)
print(vector1)
vector2=vectorize(tokens2)
print(vector2)
