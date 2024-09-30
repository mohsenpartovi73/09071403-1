
text = 'The Persian League is the largest sport event dedicated to the deprived areas of Iran.\
        The Persian League promotes peace and friendship.\
        This video was captured by one of our heroes who wishes peace.'



'''
import re
text = """The Persian League is the largest sport event dedicated to the deprived areas of Iran.
 The Persian League promotes peace and friendship. 
 This video was captured by one of our heroes who wishes peace."""

words = re.findall(r'\b[A-Z]\w*', text)
for index, word in enumerate(words, start=1):
        print(f"{index}. {word}")
'''        
'''
words = []
word = ""
for char in text:
    if char.isalpha():        
            word += char    
    else:        
        if word and word[0].isupper():
                words.append(word)
                word = ""
if word and word[0].isupper():
    words.append(word)
for index, word in enumerate(words, start=1):
    print(f"{index}. {word}")
'''    

list3 = []
text2 = text.rsplit()
print(text2)
for i in text2:
        if i[0].isupper():
                print(i)
