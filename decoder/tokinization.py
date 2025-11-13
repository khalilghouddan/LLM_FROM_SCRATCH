
#On importe le module re, qui permet de travailler avec des expressions régulières en Python.
import re


import tokenV2
#-------------------Creating vocabulary------------------------------------


#open the file with with to be close when we are donne , and using utf-8 to see the special caracters
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
#kiping the space is usful if we are traing llm to give responces
#to reduce memry i remove them

preprocessed = [item for item in preprocessed if item.strip()]


#print(preprocessed)

#print(len(preprocessed))


#-------------------Creating Token IDs------------------------------------

#we must map each token to a int in alphabitcall order
#called creating vocabulary 

all_words = sorted(set(preprocessed))
#vocab_size = len(all_words)
all_words.extend(["<|endoftext|>", "<|unk|>"])
#print(vocab_size)

vocab = {token:integer for integer,token in enumerate(all_words)}
#cle:valeur

# for i, item in enumerate(vocab.items()):
#     print(item)
#     if i >= 50:
#         break

#print (vocab)


#-------------------testing ------------------------------------


tokenizer = tokenV2.SimpleTokenizerV2(vocab)

text = """" hello It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
#print(ids)

c=tokenizer.decode(ids)
#print(c)